# Installation Guide

## Clone Repository

git clone ...

## Create Virtual Environment

python -m venv .venv

## Activate

Windows

.venv\Scripts\activate

Mac

source .venv/bin/activate

## Install Packages

pip install -r requirements.txt

## Create .env

JIRA_BASE_URL=
JIRA_EMAIL=
JIRA_API_TOKEN=
GITHUB_TOKEN=

## Verify Installation

python -m v1_single_story_testcases.main