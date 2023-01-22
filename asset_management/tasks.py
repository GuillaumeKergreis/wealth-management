import datetime
import os

from celery import shared_task

from asset_management.institutions.boursorama import BoursoramaAccountType, Boursorama, string_to_number
from asset_management.models import AccountType, Account, Institution, Transaction, AccountValue, Asset, AssetTag, \
    AssetQuantity
from market_data.data_sources.boursorama_market import BoursoramaMarket
from market_data.models import Currency, MarketAsset, DataSource, BusinessSector, Index, Marketplace


@shared_task
def synchronize_boursorama():
    bousrorama_institution = Institution.objects.get(name='Boursorama')

    for boursorama_user_institution in bousrorama_institution.user_institutions.all():
        print(boursorama_user_institution)
        boursorama = Boursorama(boursorama_user_institution.identifier, boursorama_user_institution.password)
        try:
            boursorama.connect()
            boursorama_accounts = boursorama.get_accounts()

            for boursorama_account in boursorama_accounts:
                print(boursorama_account)

                currency_eur = Currency.objects.get(code='EUR')
                print(currency_eur)
                account_type, _ = AccountType.objects.get_or_create(name=boursorama_account['type'])
                print(account_type)

                account, _ = Account.objects.get_or_create(
                    user_institution=boursorama_user_institution,
                    reference=boursorama_account['reference'],
                    defaults={
                        'name': boursorama_account['label'],
                        'value': boursorama_account['balance'],
                        'unrealized_pnl_value': None,
                        'currency': currency_eur,
                        'type': account_type,
                        'description': None,
                        'image': None,
                        'account_number': None,
                        'iban': None,
                        'bic': None
                    }
                )
                account.value = boursorama_account['balance']
                account.save()

                # TODO : add the unrealized PNL for
                if account.type.name == BoursoramaAccountType.COMPTE_A_VUE.value:
                    transactions = boursorama.get_account_cav_transactions(account.reference)
                    # TODO : Think about a better method to import transaction than replacing all the old ones
                    account.transactions.all().delete()
                    account.values.all().delete()
                    new_transactions = []
                    new_account_values = []
                    for index, transaction in transactions.iterrows():
                        new_transactions.append(Transaction(
                            account=account,
                            date=datetime.date.fromisoformat(transaction['dateOp']),
                            amount=string_to_number(transaction['amount']),
                            label=transaction['label'],
                            category=transaction['categoryParent'] + ' / ' + transaction['category'],
                            description=transaction['comment'],
                        ))
                        new_account_values.append(AccountValue(
                            account=account,
                            date=datetime.date.fromisoformat(transaction['dateOp']),
                            value=transaction['accountbalance'],
                        ))
                    Transaction.objects.bulk_create(new_transactions)
                    AccountValue.objects.bulk_create(new_account_values)
                    # TODO : update account number + iban + bic
                elif account.type.name == BoursoramaAccountType.COMPTE_SUR_LIVRET.value:
                    transactions = boursorama.get_account_csl_transactions(account.reference)
                    # TODO : Think about a better method to import transaction than replacing all the old ones
                    account.transactions.all().delete()
                    account.values.all().delete()
                    new_transactions = []
                    new_account_values = []
                    for index, transaction in transactions.iterrows():
                        new_transactions.append(Transaction(
                            account=account,
                            date=datetime.date.fromisoformat(transaction['dateOp']),
                            amount=string_to_number(transaction['amount']),
                            label=transaction['label'],
                            category=transaction['categoryParent'] + ' / ' + transaction['category'],
                            description=transaction['comment'],
                        ))
                        new_account_values.append(AccountValue(
                            account=account,
                            date=datetime.date.fromisoformat(transaction['dateOp']),
                            value=transaction['accountbalance'],
                        ))
                    Transaction.objects.bulk_create(new_transactions)
                    AccountValue.objects.bulk_create(new_account_values)
                    # TODO : update account number
                elif account.type.name == BoursoramaAccountType.PEA.value:

                    account_positions = boursorama.get_account_pea_positions(account.reference)
                    for position in account_positions:
                        asset, _ = Asset.objects.update_or_create(
                            account=account,
                            name=position.name,
                            defaults={
                                'value': position.last_price,
                                'break_even_price': position.buying_price,
                                'currency': currency_eur,
                                'quantity': position.quantity,
                            }
                        )

                        AssetQuantity.objects.update_or_create(
                            asset=asset,
                            date=datetime.date.today(),
                            defaults={
                                'quantity': position.quantity
                            }
                        )

                        print(asset)

                        if not asset.market_asset:
                            boursorama_market_asset = BoursoramaMarket.get_market_asset_by_link(position.link)
                            print(boursorama_market_asset)
                            if boursorama_market_asset:
                                marketplace = None
                                business_sector = None
                                index = None
                                if boursorama_market_asset.marketplace_name:
                                    marketplace, _ = Marketplace.objects.get_or_create(name=boursorama_market_asset.marketplace_name)
                                if boursorama_market_asset.business_sector_name:
                                    business_sector, _ = BusinessSector.objects.get_or_create(name=boursorama_market_asset.business_sector_name)
                                if boursorama_market_asset.index_name:
                                    index, _ = Index.objects.get_or_create(name=boursorama_market_asset.index_name)

                                market_asset, _ = MarketAsset.objects.update_or_create(
                                    data_source=DataSource.objects.get(name='Boursorama'),
                                    reference=boursorama_market_asset.reference,
                                    defaults={
                                        'link': boursorama_market_asset.link,
                                        'name': boursorama_market_asset.asset_name,
                                        'value': boursorama_market_asset.value,
                                        'currency': Currency.objects.get(code=boursorama_market_asset.currency_code),
                                        'description': None,
                                        'marketplace': marketplace,
                                        'isin_code': boursorama_market_asset.isin_code,
                                        'ticker': boursorama_market_asset.ticker,
                                        'image': None,
                                        'type': None,
                                        'business_sector': business_sector,
                                        'index': index
                                    }
                                )
                                if market_asset.business_sector:
                                    asset.tags.add(AssetTag.objects.get_or_create(name=market_asset.business_sector.name)[0])
                                if market_asset.index:
                                    asset.tags.add(AssetTag.objects.get_or_create(name=market_asset.index.name)[0])
                                asset.market_asset = market_asset
                                asset.save()

                    account_performances = boursorama.get_account_pea_performance(account.reference)
                    for _, account_performance in account_performances.iterrows():
                        AccountValue.objects.get_or_create(
                            account=account,
                            date=datetime.date.fromisoformat(account_performance['date']),
                            defaults={
                                'value': account_performance['valorisation']
                            }
                        )

                    # TODO : update account number + iban + bic
                elif account.type.name == BoursoramaAccountType.COMPTE_TITRE_ORDINAIRE.value:
                    pass  # TODO : update account number + iban + bic
                elif account.type.name == BoursoramaAccountType.COMPTE_FINANCIERE_EPARGNE_PILOTEE.value:
                    pass  # TODO : update account number
                elif account.type.name == BoursoramaAccountType.ASSURANCE_VIE.value:
                    pass  # TODO : update account number + positions + transactions + ...

        except Exception as e:
            print('Error during synchronization')
            print(e)

        boursorama.browser.close()
        print('Import finished')
