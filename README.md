---

# Anonymous Submission Discord Bot

This is a Discord bot designed to handle anonymous submissions, validate links, and manage data efficiently. It also includes helpful commands for managing and exporting submissions.

## Prerequisites

- Ensure you have `discord.py`, `pandas`, and `openpyxl` installed.
- Your bot token should be stored in your environment variables as `TOKEN`.

---

## Bot Setup

1. **Environment Variables**: Ensure you have your bot's token saved as `TOKEN` in your environment variables.
2. **Dependencies**: Install necessary packages using:
   ```bash
   pip install discord.py pandas openpyxl
   ```
3. **File Requirements**: 
   - The bot saves submissions in a file called `links.txt`. Make sure this file exists or the bot has permissions to create it.
   - For exporting data, the bot will generate an Excel file named `exported_data.xlsx`.

---

## Bot Commands

### 1. `!ping`

**Description**: Check the bot's latency.

**Usage**: 
``` 
!ping
```

**Response**: The bot sends an embed message displaying its latency in milliseconds.

---

### 2. `!submit`

**Description**: Initiates the submission process by sending the user a direct message with instructions.

**Usage**:
```
!submit
```

**Response**:
- **DM**: The bot sends the user a DM with submission instructions.
- **Channel Message**: Confirms that the DM has been sent.
- If the DM cannot be sent, the bot provides instructions on how to enable DMs from server members.

---

### 3. `!link <link>`

**Description**: Submit a link for approval. This command must be used in a direct message to the bot.

**Parameters**:
- `<link>`: The link to be submitted, validated by a URL pattern.

**Usage**:
```
!link https://example.com
```

**Response**:
- If valid: The bot saves the submission and provides a unique identifier.
- If invalid: The bot notifies the user that the link is incorrect.
- **Note**: This command is restricted to direct messages only.

---

### 4. `!checkuser <identifier>`

**Description**: Retrieve the user who made a submission using the unique identifier.

**Parameters**:
- `<identifier>`: The unique code provided after submission.

**Usage**:
```
!checkuser ABC12345
```

**Response**:
- If found: The bot returns the submission link and mentions the user.
- If not found: The bot notifies that no submission was found with the provided identifier.

---

### 5. `!export`

**Description**: Exports all submission data from `links.txt` into an Excel file and sends it in the Discord channel.

**Usage**:
```
!export
```

**Response**: The bot sends an Excel file named `exported_data.xlsx` containing all submission data.

---

## File Structure

- **links.txt**: A text file where all submissions are saved in the format:
  ```
  <link> | <unique identifier> | <user ID>
  ```
- **exported_data.xlsx**: An Excel file generated during the export process.

---

## Error Handling

- **DM Restrictions**: If the bot fails to send a DM, it will provide guidance on how to enable DMs from server members.
- **Submission Errors**: If an error occurs while saving a submission or exporting data, the bot will notify the user with an error message.

---

## Example Usage

### Step 1: Initiate Submission
Type `!submit` in a channel. The bot will send you a DM with instructions.

### Step 2: Submit Your Link
Send `!link <your link>` in the DM. The bot will validate your link and provide a unique code.

### Step 3: Retrieve Submission
Admins can use `!checkuser <identifier>` to find out who made a specific submission.

### Step 4: Export Data
Use `!export` to get all submissions in an Excel file.

---

## Bot Event

- **on_ready**: The bot announces in the console that it has connected to Discord.

---

### Notes

- **Permissions**: Ensure the bot has permissions to manage messages and send DMs.
- **Link Validation**: The bot uses a simple regex pattern to validate URLs. Adjust as needed for stricter validation.

---

Enjoy using EasyTourneys!
