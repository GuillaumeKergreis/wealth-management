from typing import Optional

import requests


class MonPetitPlacement:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.__access_token = self.connect()['access_token']

    def connect(self):
        """
        {
            "access_token":"eyJhbGciOiJSUz...",
            "token_type":"Bearer",
            "not-before-policy":0,
            "session_state":"987c50af-4470-4d4f-a814-5cba59e51a6f",
            "scope":"email profile"
        }
        """
        return requests.post('https://sso.monpetitplacement.fr/auth/realms/mpp-prod/protocol/openid-connect/token',
                             data={
                                 'grant_type': 'password',
                                 'client_id': 'mpp-app',
                                 'username': self.email,
                                 'password': self.password
                             }).json()

    def get_me(self):
        """
        {
            "@context": "/v1/contexts/User",
            "@id": "/v1/users/12489",
            "@type": "User",
            "id": 12489,
            "email": "gfdhtgjh465@outlook.com",
            "isTest": false,
            "lastLogin": "2023-01-07T18:23:18+00:00",
            "roles": [
                "READ_ADVICE_ITEM_SELF",
                "READ_ADVICE-DISTRIBUTION_ITEM_SELF",
                "READ_REFERENTIAL_ITEM_ALL",
                "DOWNLOAD_DOCUMENT_ITEM_SELF",
                "READ_INVEST-REQUEST_COLLECTION_SELF",
                "READ_ADVICE-FORMAT_ITEM_ALL",
                "READ_USER-KYC_ITEM_SELF",
                "READ_INVEST-REQUEST-REASON_ITEM_ALL",
                "READ_KYC-ANSWER_ITEM_ALL",
                "CREATE_USER-CONSENT_ITEM_SELF",
                "REQUEST-SIGN-CODE_USER-KYC_ITEM_SELF",
                "READ_USER-CONSENT_ITEM_SELF",
                "CREATE_USER-INVESTMENT-ACCOUNT-AMOUNT_ITEM_SELF",
                "UPDATE-ONBOARDING-CARD_USER-INVESTMENT-ACCOUNT_ITEM_SELF",
                "READ_DOCUMENT_COLLECTION_SELF",
                "READ_USER-KYC-ANSWER_ITEM_SELF",
                "READ_ADVICE-PACKAGE_COLLECTION_ALL",
                "CREATE_DOCUMENT_ITEM_SELF",
                "READ_INVEST-PROFILE_COLLECTION_ALL",
                "DELETE_INVEST-REQUEST_ITEM_SELF",
                "READ_INVEST-ORDER_ITEM_SELF",
                "UPDATE_INVEST-REQUEST_ITEM_SELF",
                "READ-AVAILABLE_INVEST-PROFILE_COLLECTION_SELF",
                "READ_USER-INVESTMENT-ACCOUNT_ITEM_SELF",
                "READ_USER-CALENDLY-EVENT_COLLECTION_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-ADVICE-DTO_ITEM_SELF",
                "READ_USER-FINANCIAL-CAPITAL_ITEM_SELF",
                "READ_USER-INVESTMENT-VALUE_ITEM_SELF",
                "READ_USER_ITEM_SELF",
                "READ_GOAL_COLLECTION_ALL",
                "READ_USER-ADDRESS_ITEM_SELF",
                "READ_KYC-QUESTION_ITEM_ALL",
                "READ_INVEST-ORDERS-DETAIL_ITEM_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-BILL_ITEM_SELF",
                "READ_KYC-ANSWER_COLLECTION_ALL",
                "READ_USER-INVESTMENT-ACCOUNT-PRODUCT_ITEM_SELF",
                "READ_USER-FINANCIAL-CAPITAL_COLLECTION_SELF",
                "CONFIRM_INVEST-REQUEST_ITEM_SELF",
                "UPDATE-DETAILS_INVEST-REQUEST_ITEM_SELF",
                "READ_INVEST-REQUEST-REASON_COLLECTION_ALL",
                "READ_USER-INVESTMENT-VALUE_COLLECTION_SELF",
                "READ_PRODUCT-VALUE_COLLECTION_ALL",
                "READ_ADVICE-FORMAT_COLLECTION_ALL",
                "READ_INVEST-PROFILE-CATEGORY_ITEM_ALL",
                "READ_COUPON_ITEM_SELF",
                "READ_INVESTMENT-BILL_ITEM_SELF",
                "READ_COUPON_COLLECTION_SELF",
                "READ_KYC-QUESTION_COLLECTION_ALL",
                "READ_USER-CALENDLY-EVENT_ITEM_SELF",
                "READ_DOCUMENT_ITEM_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-MONTHLY-INVESTMENT_ITEM_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-AMOUNT_ITEM_SELF",
                "READ_INVEST-REQUEST_ITEM_SELF",
                "UPDATE_USER-INVESTMENT-ACCOUNT_ITEM_SELF",
                "UPDATE_USER-KYC_ITEM_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-PRODUCT_COLLECTION_SELF",
                "READ_UNIVERSIGN-TRANSACTION_COLLECTION_SELF",
                "READ_PRODUCT_ITEM_ALL",
                "SIGN_USER-KYC_ITEM_SELF",
                "READ_ADVICE-SUBPACKAGE_ITEM_ALL",
                "CREATE_USER-INVESTMENT-ACCOUNT-CALL-BACK_ITEM_ALL",
                "READ_SETTING_ITEM_ALL",
                "READ_USER-CONSENT_COLLECTION_SELF",
                "CREATE_INVEST-REQUEST_ITEM_SELF",
                "READ_USER-INVESTMENT-ACCOUNT-MONTHLY-INVESTMENT_COLLECTION_SELF",
                "UPDATE_USER-ORIGIN_ITEM_SELF",
                "UPDATE_USER_ITEM_SELF",
                "READ_USER-COUPON_COLLECTION_SELF",
                "REMINDER_USER-COUPON_ITEM_SELF",
                "UPDATE_INVEST-REQUEST-PLACE_ITEM_SELF",
                "READ_KYC-CATEGORY_COLLECTION_ALL",
                "READ_INVESTMENT-BILL_COLLECTION_SELF",
                "READ_GOAL_ITEM_ALL",
                "READ_INVEST-REQUEST-DETAIL_ITEM_SELF",
                "READ_INVESTMENT-ACCOUNT-PROVIDER_ITEM_ALL",
                "READ_USER-INVESTMENT-ACCOUNT-BILL_COLLECTION_SELF",
                "RESUME_INVEST-REQUEST_ITEM_SELF",
                "READ_USER-SENSIBLE-DATA_COLLECTION_SELF",
                "READ-AVAILABLE_PRODUCT_COLLECTION_SELF",
                "CREATE_USER-KYC-ANSWER_ITEM_SELF",
                "READ_INVEST-PROFILE_ITEM_ALL",
                "READ_INVEST-PROFILE-CATEGORY_COLLECTION_ALL",
                "READ_PRODUCT_COLLECTION_ALL",
                "READ_USER-COUPON_ITEM_SELF",
                "READ_UNIVERSIGN-TRANSACTION_ITEM_SELF",
                "READ_PRODUCT-VALUE_ITEM_ALL",
                "READ_REFERENTIAL_COLLECTION_ALL",
                "READ_ADVICE-PACKAGE_ITEM_ALL",
                "READ_USER-INVESTMENT-ORDER_ITEM_SELF",
                "READ_USER-SENSIBLE-DATA_ITEM_SELF",
                "READ_ADVICE-SUBPACKAGE_COLLECTION_ALL",
                "SEND-CONFIRMATION-EMAIL_USER_ITEM_SELF",
                "READ_KYC-CATEGORY_ITEM_ALL",
                "READ_INVEST-ORDER_COLLECTION_SELF",
                "READ_AFFILIATE-PROVIDER_ITEM_ALL"
            ],
            "firstname": "FirstName",
            "lastname": "LastName",
            "gender": "man",
            "phone": "+33612345678",
            "cgvAccepted": true,
            "validatedAt": "2020-11-25T18:59:44+00:00",
            "birthdate": "1998-03-17T00:00:00+00:00",
            "nationality": "fr",
            "viewPreference": "invest-profile",
            "investmentAccounts": [
                {
                    "@id": "/v1/user_investment_accounts/12680",
                    "@type": "UserInvestmentAccount",
                    "id": "12680",
                    "status": "active",
                    "reference": "4058991",
                    "watermark": 9777.33,
                    "watermarkedAt": "2022-12-14T00:00:00+00:00",
                    "providerProjectId": "27767",
                    "providerContractId": "4058991",
                    "statusProvider": "Contrat ouvert",
                    "profile": "co-pilot",
                    "incompatible": false,
                    "appointmentRequired": false,
                    "effectiveDate": "2020-12-10T00:00:00+00:00",
                    "signatureDate": "2020-12-01T09:53:16+00:00",
                    "nextMonthlyPaymentDate": "2023-01-10T00:00:00+00:00",
                    "lastProviderKycUpdateAt": "2021-12-03T00:00:00+00:00",
                    "provider": {
                        "@id": "/v1/investment_account_providers/apicil",
                        "@type": "InvestmentAccountProvider",
                        "id": "4",
                        "name": "Apicil",
                        "slug": "apicil",
                        "position": "3",
                        "enabled": true,
                        "minimumFirstInvestment": 1000,
                        "minimumFirstInvestmentMonthly": 500,
                        "minimumInvestmentMonthly": 100,
                        "uuid": "b0c38008-afbc-49fa-a9d4-6127aba5f651",
                        "createdAt": "2019-12-19T16:27:59+00:00",
                        "updatedAt": "2021-12-15T15:24:32+00:00"
                    },
                    "userKycs": [
                        "/v1/user_kycs/1293"
                    ],
                    "hidden": false,
                    "duration": 5,
                    "userInvestmentAccountCallBack": [],
                    "uuid": "f221dfb6-9a14-493d-921e-8fe8857177f6",
                    "createdAt": "2020-11-25T18:58:56+00:00",
                    "updatedAt": "2022-12-16T16:48:48+00:00",
                    "userKyc": "/v1/user_kycs/1293"
                }
            ],
            "userSensibleData": [
                "/v1/user_sensible_datas/1293"
            ],
            "crispId": "929c9198-b9fa-453c-ae8a-baa48b965633",
            "crispSegments": [
                "client",
                "co-pilote",
                "vidéo perso",
                "apicil"
            ],
            "uuid": "505ed561-0518-4f57-87bc-5cf0a6493a01",
            "createdAt": "2020-11-25T18:58:56+00:00",
            "updatedAt": "2023-01-07T18:23:18+00:00",
            "affiliationLevel": "Beginner",
            "affiliationAlreadyClientUserCount": 0,
            "affiliationTotalUserCount": 0,
            "affiliationSavingsPercent": 15.000000000000002,
            "affiliationSavingPercentWithoutGodChilds": 15.000000000000002,
            "username": "fwegt156@outlook.com"
        }
        """
        return requests.get('https://api.monpetitplacement.fr/v1/me',
                            headers={
                                'authorization': f'Bearer {self.__access_token}'
                            }).json()

    def get_user_financial_capital(self, investment_account_id: str):
        """
        {
            "@context": "/v1/contexts/UserFinancialCapital",
            "@id": "/v1/user_financial_capitals/12680",
            "@type": "UserFinancialCapital",
            "id": "12680",
            "amount": 83.35,
            "performance": -1.13,
            "numberPendingOperations": 0,
            "buyAmount": 0,
            "sellAmount": 0,
            "exchangeAmount": 0,
            "effectiveDate": "2023-01-07T00:00:00+00:00",
            "totalInvestAmount": 94,
            "initialInvestmentPending": false,
            "operationValuatedAt": null,
            "isBeingDailyProcessed": false,
            "gain": -10.65
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/user_financial_capital',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_user_investment_account_products(self, investment_account_id: str):
        """
        {
            "@context": "/v1/contexts/UserInvestmentAccountProduct",
            "@id": "/v1/user_investment_accounts/12680/user_investment_account_products",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/user_investment_account_products/12680_21",
                    "@type": "UserInvestmentAccountProduct",
                    "id": "12680_21",
                    "productId": 21,
                    "name": "Comgest • Monde",
                    "investProfileCategories": [
                        "/v1/invest_profile_categories/3",
                        "/v1/invest_profile_categories/4"
                    ],
                    "amount": 19.74,
                    "pendingTransaction": false,
                    "performance": -8.19,
                    "securityUnits": 0.8132,
                    "averageAcquisitionAmount": 2608.75
                }
            ]
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/user_investment_account_products',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_user_investment_values(self, investment_account_id: str, page_number: str, product_id: Optional[int]):
        """
        {
            "@context": "/v1/contexts/UserInvestmentValue",
            "@id": "/v1/user_investment_accounts/12680/user_investment_values",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/user_investment_values/64512143",
                    "@type": "UserInvestmentValue",
                    "id": "64512143",
                    "type": "account-daily",
                    "date": "2023-01-07T00:00:00+00:00",
                    "amount": 83.35,
                    "averageAcquisitionAmount": null,
                    "securityUnits": null,
                    "performance": -1.13,
                    "investedAmount": 9400,
                    "approximation": false,
                    "product": null,
                    "userInvestmentAccount": "/v1/user_investment_accounts/12680",
                    "createdAt": "2023-01-07T07:52:16+00:00",
                    "updatedAt": "2023-01-07T07:52:16+00:00",
                    "owner": "/v1/users/12489"
                }
            ],
            "hydra:totalItems": 594,
            "hydra:view": {
                "@id": "/v1/user_investment_accounts/12680/user_investment_values?date%5Bstrictly_after%5D=2020-12-10&limit=200&type=account-daily&page=1",
                "@type": "hydra:PartialCollectionView",
                "hydra:first": "/v1/user_investment_accounts/12680/user_investment_values?date%5Bstrictly_after%5D=2020-12-10&limit=200&type=account-daily&page=1",
                "hydra:last": "/v1/user_investment_accounts/12680/user_investment_values?date%5Bstrictly_after%5D=2020-12-10&limit=200&type=account-daily&page=3",
                "hydra:next": "/v1/user_investment_accounts/12680/user_investment_values?date%5Bstrictly_after%5D=2020-12-10&limit=200&type=account-daily&page=2"
            }
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/user_investment_values?type=account-daily&page={page_number}&limit=200&date%5Bstrictly_after%5D=2020-12-10{f"&product={product_id}" if product_id else ""}',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_investment_bill(self, investment_account_id: str):
        """
        {
            "@context": "/v1/contexts/InvestmentBill",
            "@id": "/v1/user_investment_accounts/12680/investment_bills",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/investment_bills/71305",
                    "@type": "InvestmentBill",
                    "isMandatory": true,
                    "id": 71305,
                    "status": "generated",
                    "startAt": "2022-09-14T00:00:00+00:00",
                    "endAt": "2022-12-14T00:00:00+00:00",
                    "totalExcludingTax": 0,
                    "vat": 0,
                    "finalCapital": 82.68,
                    "watermark": 977733,
                    "gain": -15.65,
                    "commissionRate": 11.69,
                    "discountRatio": 85,
                    "investmentAccount": "/v1/user_investment_accounts/12680",
                    "document": "/v1/documents/316846",
                    "uuid": "7dfd0da9-c71f-4cfe-b263-54e187c6232a",
                    "createdAt": "2022-12-16T16:48:40+00:00",
                    "updatedAt": "2022-12-16T16:48:48+00:00",
                    "totalIncludingTax": 0
                }
            ],
            "hydra:totalItems": 8
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/investment_bills',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_invest_requests(self, investment_account_id: str):
        """
        {
            "@context": "/v1/contexts/InvestRequest",
            "@id": "/v1/user_investment_accounts/12680/invest_requests",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/invest_requests/58319",
                    "@type": "InvestRequest",
                    "id": "58319",
                    "reference": "612744",
                    "frequency": "periodic",
                    "type": "update-monthly-investment",
                    "status": "completed",
                    "error": null,
                    "amountOrdered": 300,
                    "originFunds": [
                        {
                            "date": null,
                            "slug": "income",
                            "percent": 100
                        }
                    ],
                    "consentGivenAt": "2022-04-28T08:47:41+00:00",
                    "taxOption": null,
                    "investRequestDetails": [
                        {
                            "@id": "/v1/invest_request_details/371444",
                            "@type": "InvestRequestDetail",
                            "id": 371444,
                            "type": "buy",
                            "amountOrdered": 57,
                            "product": {
                                "@id": "/v1/products/21",
                                "@type": "Product",
                                "id": "21",
                                "name": "Comgest • Monde",
                                "slug": "comgest-monde-eur-c",
                                "isin": "FR0000284689",
                                "generaliAmendmentUri": null,
                                "apicilAmendmentUri": null,
                                "uuid": "6d914fef-c697-4886-9ccf-c0a2fbf8f2f9",
                                "createdAt": "2019-12-19T16:28:01+00:00",
                                "updatedAt": "2022-12-20T12:04:54+00:00"
                            },
                            "investProfile": {
                                "@id": "/v1/invest_profiles/49",
                                "@type": "InvestProfile",
                                "id": 49,
                                "name": "Intrépide",
                                "slug": "intrepide-2022-04-01"
                            },
                            "uuid": "75ec8d01-e2b4-4b78-8e6b-83c50ba9851c",
                            "createdAt": "2022-04-28T08:45:22+00:00",
                            "updatedAt": "2022-04-28T08:45:22+00:00"
                        }
                    ],
                    "userInvestmentAccount": "/v1/user_investment_accounts/12680",
                    "investOrders": [
                        {
                            "@id": "/v1/invest_orders/3142413",
                            "@type": "InvestOrder",
                            "id": "3142413",
                            "status": "completed",
                            "amountDebited": 300,
                            "processedAt": "2022-08-10T00:00:00+00:00",
                            "valuatedAt": "2022-08-12T00:00:00+00:00"
                        }
                    ],
                    "currentPlace": "end",
                    "reason": null,
                    "reasonDetail": null,
                    "uuid": "7bbe0612-20c4-4243-8f1b-68156d949185",
                    "createdAt": "2022-04-28T08:44:13+00:00",
                    "updatedAt": "2022-05-11T08:34:08+00:00",
                    "abandoned": false
                }
            ],
            "hydra:totalItems": 4,
            "hydra:view": {
                "@id": "/v1/user_investment_accounts/12680/invest_requests?limit=200",
                "@type": "hydra:PartialCollectionView"
            }
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/invest_requests?page=1&limit=200',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_invest_orders(self, investment_account_id: str):
        """
        {
            "@context": "/v1/contexts/InvestOrder",
            "@id": "/v1/user_investment_accounts/12680/invest_orders",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/invest_orders/3202458",
                    "@type": "InvestOrder",
                    "id": "3202458",
                    "reference": "55945862",
                    "type": "buy",
                    "subType": "monthly-investment",
                    "status": "completed",
                    "amountOrdered": 300,
                    "amountDebited": 300,
                    "processedAt": "2022-12-12T00:00:00+00:00",
                    "valuatedAt": "2022-12-14T00:00:00+00:00",
                    "userInvestmentAccount": "/v1/user_investment_accounts/12680",
                    "investOrderDetails": [
                        {
                            "@id": "/v1/invest_order_details/27363367",
                            "@type": "InvestOrderDetail",
                            "id": "27363367",
                            "type": "buy",
                            "status": "completed",
                            "amountOrdered": 60,
                            "amountDebited": 60,
                            "securityUnitReceived": "0.30380",
                            "securityUnitValue": 197.47,
                            "product": {
                                "@id": "/v1/products/81",
                                "@type": "Product",
                                "id": "81",
                                "name": "Rothschild • Conviction Equity Value Euro",
                                "slug": "rco-conviction-equity-value-euro-eur-c",
                                "isin": "FR0010187898",
                                "uuid": "932fde83-1271-490a-969d-a400f665dac4",
                                "createdAt": "2021-04-06T12:48:29+00:00",
                                "updatedAt": "2022-12-20T12:04:54+00:00",
                                "investProfiles": [
                                    "/v1/invest_profiles/4",
                                    "/v1/invest_profiles/42",
                                    "/v1/invest_profiles/48",
                                    "/v1/invest_profiles/49"
                                ]
                            },
                            "uuid": "fa44b4b8-edc0-4192-9413-774a31c16458",
                            "createdAt": "2022-12-13T08:33:25+00:00",
                            "updatedAt": "2023-01-07T07:52:16+00:00"
                        }
                    ],
                    "userInvestmentAccountAmount": null,
                    "uuid": "c687a5e8-f55a-4c1a-9bdf-4d934e2ba16d",
                    "createdAt": "2022-12-13T08:33:25+00:00",
                    "updatedAt": "2022-12-16T08:22:24+00:00"
                }
            ],
            "hydra:totalItems": 26,
            "hydra:view": {
                "@id": "/v1/user_investment_accounts/12680/invest_orders?limit=200",
                "@type": "hydra:PartialCollectionView"
            }
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/user_investment_accounts/{investment_account_id}/invest_orders?page=1&limit=200',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()

    def get_product_values(self, product_id: str):
        """
        {
            "@context": "/v1/contexts/ProductValue",
            "@id": "/v1/product_values",
            "@type": "hydra:Collection",
            "hydra:member": [
                {
                    "@id": "/v1/product_values/252523",
                    "@type": "ProductValue",
                    "id": "252523",
                    "date": "2023-01-07T00:00:00+00:00",
                    "amount": 2395.15,
                    "product": "/v1/products/21",
                    "uuid": "66471b4a-1376-4038-88f9-9d38f25420a9",
                    "createdAt": "2023-01-07T07:35:28+00:00",
                    "updatedAt": "2023-01-07T07:35:28+00:00"
                }

            ],
            "hydra:totalItems": 3621,
            "hydra:view": {
                "@id": "/v1/product_values?limit=200&product=21&page=1",
                "@type": "hydra:PartialCollectionView",
                "hydra:first": "/v1/product_values?limit=200&product=21&page=1",
                "hydra:last": "/v1/product_values?limit=200&product=21&page=19",
                "hydra:next": "/v1/product_values?limit=200&product=21&page=2"
            },
            "hydra:search": {
                "@type": "hydra:IriTemplate",
                "hydra:template": "/v1/product_values{?product,product[],product.isin,product.isin[],date[before],date[strictly_before],date[after],date[strictly_after]}",
                "hydra:variableRepresentation": "BasicRepresentation",
                "hydra:mapping": [
                    {
                        "@type": "IriTemplateMapping",
                        "variable": "product",
                        "property": "product",
                        "required": false
                    }
                ]
            }
        }
        """
        return requests.get(
            f'https://api.monpetitplacement.fr/v1/product_values?page=1&limit=200&product={product_id}',
            headers={
                'authorization': f'Bearer {self.__access_token}'
            }).json()
