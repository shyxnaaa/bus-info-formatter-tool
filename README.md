# bus-info-formatter-tool
A simple Python utility that converts raw bus information strings into structured JSON format.

## Features
- Accepts **multiple entries at once**
- Input can be:
  - A single string with entries separated by `;`
  - A list of entry strings
- Outputs structured **JSON**
- Skips invalid entries automatically

## 📂 Example Input
```text
"202, Rohtak, Delhi, 8:45 AM, 50; 105, Panipat, Ambala, 10:00 AM, 60; 410, Chandigarh, Delhi, 6:15 PM, 75"
