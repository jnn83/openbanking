# openbanking
Openbanking 'Open Data' API data published by UK banks 

This is a hobby project I started in late 2019, to create a panel dataset from the publicly available OpenBanking APIs of retail banks in the United Kingdom. Every day at midnight, I poll all the banks' Open Data APIs and store a copy of any new or updated data. You can download that data here in raw format. Soon, you'll be able to download the data in a panel dataset (.csv) format too.

## What is Openbanking data?

See [https://www.openbanking.org.uk/] for more information on Openbanking. Openbanking is a much broader initiative than the publicly available API data, but for obvious reasons I'm only capturing publicly available data. The publicly available data covers the following information on a bank's products and services:
- Personal current accounts
- Business current accounts 
- Business (SME) credit cards 
- Business (SME) unsecured loans
- ATM locations
- Branch locations

## Which banks' data is available?

The following banks' data is included:
- Barclays
- Bank of Scotland (BOS)
- Halifax
- HSBC
- Lloyds
- Nationwide
- Natwest
- Royal Bank of Scotland (RBS)
- Santander
- Ulster

Note that banks may not provide data on all the above products, for example if they don't offer these products.

## What format is the data in?

The raw data is in JSON format, the format in which it is served by the banks' APIs. The data is structured according to the OpenBanking Open Data API standards [https://openbankinguk.github.io/opendata-api-docs-pub/]. I have performed minimal data cleaning to ensure all historically downloaded data meets the standards. For transparency, I have made my cleaning code available in this project.

## What can I use the data for?

Whatever you like. I am only resharing freely available data. See here for the Openbanking open data licence: [https://www.openbanking.org.uk/wp-content/uploads/2017/02/Open-Licence.pdf].
