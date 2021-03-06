#!/usr/bin/env python3

#
# Feedstyl (http://git.io/feedstyl)
# Licensed under the MIT License.
#

from sys import argv
import feedparser

# Error handlers
# --------------

# Check for incorrect usage
if len(argv) == 1:
  print("URL is missing.\n")
  url = input("Enter it: ")
# Default case
else:
  url = argv[1]

# Fix broken links without protocol
if not (url.startswith("http://") or url.startswith("https://")):
  url = "http://" + url

# Configuration
# -------------

# Indent
indent_lenght = 2
indent = " " * indent_lenght

# Truncation (depends on indent)
feed_trunc = 59
entry_trunc = 56

# Helper functions
# ----------------

# Bold decoration
def bold(string):
  return "\033[1m" + string + "\033[0m"

# Truncation
def trunc(trunc, string):
  if len(string) > trunc:
    string = string[:trunc] + "..."
  return string

# Display data
# ------------

print()

# Feed data
data = feedparser.parse(url)

# Display feed properties
def feed():
  print(bold("Feed title: ") + data.feed.title)
  if "description" in data.feed:
    print(bold("Feed description: ") + trunc(feed_trunc, data.feed.description))
  print(bold("Feed link: ") + data.feed.link + "\n")

# Display entries properties
def entries():
  print(bold("Feed entries:\n"))
  for entry in data.entries:
    print(indent + bold("Entry title: ") + entry.title)
    if "description" in entry:
      print(indent + bold("Entry description: ") + \
            trunc(entry_trunc, entry.description))
    print(indent + bold("Entry link: ") + entry.link + "\n")

# Display data only when ran as main
def main():
  feed()
  entries()

if __name__ == "__main__":
  main()
