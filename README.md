# notion-test
Test environment for editing MAO database in Notion

## Required secrets

Write these secrets to `.env` file (`key=value` format) before running scripts (ask Taniguchi for the values).

Key | Description
--- | ---
`NOTION_TOKEN` | Notion internal integration secret
`DATABASE_ID` | Database ID of the MAO data

## Available scripts

Script | Description
--- | ---
`scrips/connect.py` | Test connection to the database
