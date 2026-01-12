# EasyTourneys

**EasyTourneys** is a streamlined Discord bot designed to manage anonymous tournament submissions. It automates the process of collecting entry links via Direct Messages, validating URLs, and generating unique identification codes for participants.

[Download Latest Release](https://github.com/nthnerr/EasyTourneys/releases)

---

## Why use EasyTourneys?

* **Anonymous Submissions:** Users submit their entries via Direct Messages to keep links and identifiable data out of public server channels.
* **Unique ID Generation:** Automatically assigns a custom tracking code to every submission for easy verification and organization.
* **Automated Validation:** Built-in URL checking ensures participants submit valid links rather than plain text or errors.
* **Easy Data Export:** Replaces manual spreadsheets by allowing organizers to export all submissions into a professional Excel file with one command.

## Installation

1. **Download** and extract the latest EasyTourneys release.
2. **Configure Token:** Set your Discord Bot Token as an environment variable named `TOKEN`.
3. **Install Dependencies:** Run `pip install discord.py pandas openpyxl` in your terminal.
4. **Launch:** Run the script using `python EasyTourneys.py` to bring the bot online.

## How to Use

1. **!submit**: Users type this in the server to receive submission instructions privately via DM.
2. **!link [url]**: Users send their entry link to the bot via DM to receive their **Unique Code**.
3. **!checkuser [code]**: Organizers use this in the server to find the Discord user associated with a specific code.
4. **!export**: Instantly generates and uploads an `.xlsx` file containing all submission data.

## Technical Specs
* **Language:** Python 3.x
* **Library:** Discord.py
* **Data Handling:** Pandas & Openpyxl
* **Platform:** Compatible with any environment supporting Python.

---
*Created by [nthnerr](https://github.com/nthnerr)*
