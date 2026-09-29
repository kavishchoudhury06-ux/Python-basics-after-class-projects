"""
A4 — Book Library Manager
Assignment for L4 — File I/O with JSON & CSV
Concept: JSON read/write, CSV export, nested dicts, search, sort, filter, data persistence
Time: 20–25 minutes | Pure Python — zero external libraries
"""

import json
import csv
import os
from datetime import datetime

print("=" * 62)
print("       📚 BOOK LIBRARY MANAGER — FILE I/O MASTERY")
print("=" * 62)

# ── DATASET ──────────────────────────────────────────────────
# A collection of 25 books with rich metadata

LIBRARY = [
    {"id": 1,  "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams",
    "genre": "Sci-Fi",   "year": 1979, "pages": 193, "rating": 4.8, "read": True},
    {"id": 2,  "title": "1984",                                  "author": "George Orwell",
    "genre": "Dystopia", "year": 1949, "pages": 328, "rating": 4.9, "read": True},
    {"id": 3,  "title": "Dune",                                  "author": "Frank Herbert",
    "genre": "Sci-Fi",   "year": 1965, "pages": 412, "rating": 4.7, "read": False},
    {"id": 4,  "title": "The Great Gatsby",                      "author": "F. Scott Fitzgerald",
    "genre": "Classic",  "year": 1925, "pages": 180, "rating": 3.9, "read": True},
    {"id": 5,  "title": "To Kill a Mockingbird",                 "author": "Harper Lee",
    "genre": "Classic",  "year": 1960, "pages": 281, "rating": 4.8, "read": False},
    {"id": 6,  "title": "The Alchemist",                         "author": "Paulo Coelho",
    "genre": "Fiction",  "year": 1988, "pages": 163, "rating": 4.6, "read": True},
    {"id": 7,  "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling",
    "genre": "Fantasy",  "year": 1997, "pages": 309, "rating": 4.7, "read": True},
    {"id": 8,  "title": "The Lord of the Rings",                 "author": "J.R.R. Tolkien",
    "genre": "Fantasy",  "year": 1954, "pages": 1178,"rating": 4.9, "read": False},
    {"id": 9,  "title": "Brave New World",                       "author": "Aldous Huxley",
    "genre": "Dystopia", "year": 1932, "pages": 311, "rating": 4.5, "read": True},
    {"id": 10, "title": "The Catcher in the Rye",               "author": "J.D. Salinger",
    "genre": "Classic",  "year": 1951, "pages": 277, "rating": 3.8, "read": False},
    {"id": 11, "title": "Foundation",                            "author": "Isaac Asimov",
    "genre": "Sci-Fi",   "year": 1951, "pages": 255, "rating": 4.7, "read": False},
    {"id": 12, "title": "Sapiens",                               "author": "Yuval Noah Harari",
    "genre": "Non-Fiction","year":2011,"pages": 443, "rating": 4.6, "read": True},
    {"id": 13, "title": "Atomic Habits",                         "author": "James Clear",
    "genre": "Non-Fiction","year":2018,"pages": 320, "rating": 4.8, "read": True},
    {"id": 14, "title": "The Hobbit",                            "author": "J.R.R. Tolkien",
    "genre": "Fantasy",  "year": 1937, "pages": 310, "rating": 4.7, "read": True},
    {"id": 15, "title": "Pride and Prejudice",                   "author": "Jane Austen",
    "genre": "Classic",  "year": 1813, "pages": 432, "rating": 4.5, "read": False},
    {"id": 16, "title": "The Pragmatic Programmer",              "author": "Andrew Hunt",
    "genre": "Tech",     "year": 1999, "pages": 352, "rating": 4.7, "read": True},
    {"id": 17, "title": "Clean Code",                            "author": "Robert C. Martin",
    "genre": "Tech",     "year": 2008, "pages": 431, "rating": 4.5, "read": False},
    {"id": 18, "title": "Deep Work",                             "author": "Cal Newport",
    "genre": "Non-Fiction","year":2016,"pages": 296, "rating": 4.6, "read": True},
    {"id": 19, "title": "The Martian",                           "author": "Andy Weir",
    "genre": "Sci-Fi",   "year": 2011, "pages": 369, "rating": 4.7, "read": True},
    {"id": 20, "title": "Ender's Game",                          "author": "Orson Scott Card",
    "genre": "Sci-Fi",   "year": 1985, "pages": 226, "rating": 4.8, "read": False},
    {"id": 21, "title": "The Psychology of Money",              "author": "Morgan Housel",
    "genre": "Non-Fiction","year":2020,"pages": 256, "rating": 4.7, "read": True},
    {"id": 22, "title": "Fahrenheit 451",                        "author": "Ray Bradbury",
    "genre": "Dystopia", "year": 1953, "pages": 249, "rating": 4.4, "read": False},
    {"id": 23, "title": "The Name of the Wind",                  "author": "Patrick Rothfuss",
    "genre": "Fantasy",  "year": 2007, "pages": 662, "rating": 4.6, "read": True},
    {"id": 24, "title": "Thinking, Fast and Slow",              "author": "Daniel Kahneman",
    "genre": "Non-Fiction","year":2011,"pages": 499, "rating": 4.5, "read": False},
    {"id": 25, "title": "The Girl with the Dragon Tattoo",       "author": "Stieg Larsson",
    "genre": "Thriller", "year": 2005, "pages": 465, "rating": 4.4, "read": True},
]

# ── STEP 1 — SAVE TO JSON ────────────────────────────────────
print("\n💾 STEP 1 — SAVING LIBRARY TO JSON")
with open("library.json", "w", encoding="utf-8") as f:
    json.dump({"library": LIBRARY,
              "metadata": {
                  "total_books": len(LIBRARY),
                  "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                  "version": "1.0"
              }}, f, indent=2)
print(f"  ✅ Saved {len(LIBRARY)} books to library.json")

# ── STEP 2 — LOAD BACK AND VERIFY ────────────────────────────
print("\n📂 STEP 2 — LOADING FROM JSON")
with open("library.json", "r", encoding="utf-8") as f:
    data = json.load(f)

books    = data["library"]
metadata = data["metadata"]
print(f"  ✅ Loaded {len(books)} books successfully")
print(f"  Created at: {metadata['created_at']}")

# ── STEP 3 — BASIC STATS ─────────────────────────────────────
print("\n📊 STEP 3 — LIBRARY STATISTICS")
print("-" * 50)

total_pages  = sum(b["pages"] for b in books)
avg_rating   = sum(b["rating"] for b in books) / len(books)
read_books   = [b for b in books if b["read"]]
unread_books = [b for b in books if not b["read"]]
genres       = {}
for b in books:
    genres[b["genre"]] = genres.get(b["genre"], 0) + 1

print(f"  Total books     : {len(books)}")
print(f"  Books read      : {len(read_books)} ({len(read_books)/len(books)*100:.0f}%)")
print(f"  To-read list    : {len(unread_books)}")
print(f"  Total pages     : {total_pages:,}")
print(f"  Avg pages/book  : {total_pages//len(books)}")
print(f"  Avg rating      : {avg_rating:.2f} ⭐")
print(f"\n  Genre breakdown:")
for genre, count in sorted(genres.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"    {genre:<15}: {bar} ({count})")

# ── STEP 4 — SEARCH FUNCTION ──────────────────────────────────
print("\n🔍 STEP 4 — SEARCH & FILTER")
print("-" * 50)

def search_books(books, genre=None, min_rating=None, read_status=None, keyword=None):
    """Multi-filter book search."""
    results = books[:]
    if genre:
        results = [b for b in results if b["genre"] == genre]
    if min_rating:
        results = [b for b in results if b["rating"] >= min_rating]
    if read_status is not None:
        results = [b for b in results if b["read"] == read_status]
    if keyword:
        kw = keyword.lower()
        results = [b for b in results if kw in b["title"].lower()
                  or kw in b["author"].lower()]
    return results

# Search 1: Sci-Fi books rated 4.7+
scifi_top = search_books(books, genre="Sci-Fi", min_rating=4.7)
print(f"  Sci-Fi books rated 4.7+ : {len(scifi_top)}")
for b in scifi_top:
    print(f"    → {b['title']} ({b['year']}) — {b['rating']}⭐")

# Search 2: Unread books over 400 pages
long_unread = search_books(books, min_rating=None, read_status=False)
long_unread = [b for b in long_unread if b["pages"] > 400]
print(f"\n  Unread books (400+ pages): {len(long_unread)}")
for b in long_unread:
    print(f"    → {b['title']} — {b['pages']} pages | {b['rating']}⭐")

# Search 3: Keyword search
tolkien = search_books(books, keyword="tolkien")
print(f"\n  Books by/about 'tolkien' : {len(tolkien)}")
for b in tolkien:
    print(f"    → {b['title']} ({b['pages']} pages)")

# ── STEP 5 — SORT & RANK ──────────────────────────────────────
print("\n🏆 STEP 5 — RANKINGS")
print("-" * 50)

# Top 5 by rating
top_rated = sorted(books, key=lambda b: b["rating"], reverse=True)[:5]
print("  Top 5 by rating:")
for i, b in enumerate(top_rated, 1):
    print(f"    {i}. {b['title']:<42} {b['rating']}⭐")

# Longest books
print("\n  Top 3 longest books:")
longest = sorted(books, key=lambda b: b["pages"], reverse=True)[:3]
for i, b in enumerate(longest, 1):
    print(f"    {i}. {b['title']:<42} {b['pages']} pages")

# Oldest books
print("\n  5 oldest books:")
oldest = sorted(books, key=lambda b: b["year"])[:5]
for b in oldest:
    print(f"    • {b['title']:<42} ({b['year']})")

# ── STEP 6 — ADD NEW BOOK + UPDATE JSON ───────────────────────
print("\n✏️  STEP 6 — ADDING A NEW BOOK")
new_book = {
    "id"    : len(books) + 1,
    "title" : "Python Crash Course",
    "author": "Eric Matthes",
    "genre" : "Tech",
    "year"  : 2019,
    "pages" : 544,
    "rating": 4.7,
    "read"  : False,
}
books.append(new_book)
data["library"]  = books
data["metadata"]["total_books"] = len(books)
data["metadata"]["updated_at"]  = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("library.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print(f"  ✅ Added: '{new_book['title']}' (now {len(books)} books total)")

# ── STEP 7 — EXPORT REPORTS TO CSV ────────────────────────────
print("\n💾 STEP 7 — EXPORTING CSV REPORTS")

# Full library CSV
fields = ["id", "title", "author", "genre", "year", "pages", "rating", "read"]
with open("full_library.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(books)
print(f"  ✅ Saved: full_library.csv ({len(books)} books)")

# To-read list CSV
to_read = sorted([b for b in books if not b["read"]],
                key=lambda b: b["rating"], reverse=True)
with open("to_read_list.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(to_read)
print(f"  ✅ Saved: to_read_list.csv ({len(to_read)} books)")

# Genre stats CSV
genre_report = []
for genre in sorted(genres.keys()):
    genre_books = [b for b in books if b["genre"] == genre]
    genre_report.append({
        "genre"       : genre,
        "count"       : len(genre_books),
        "avg_rating"  : round(sum(b["rating"] for b in genre_books)/len(genre_books), 2),
        "avg_pages"   : round(sum(b["pages"]  for b in genre_books)/len(genre_books)),
        "read_count"  : sum(1 for b in genre_books if b["read"]),
        "unread_count": sum(1 for b in genre_books if not b["read"]),
    })
with open("genre_stats.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=genre_report[0].keys())
    writer.writeheader()
    writer.writerows(genre_report)
print(f"  ✅ Saved: genre_stats.csv ({len(genre_report)} genres)")

# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 62)
print(f"  Final library size     : {len(books)} books")
print(f"  Files created          : library.json, full_library.csv,")
print(f"                           to_read_list.csv, genre_stats.csv")
print(f"  Highest rated book     : {top_rated[0]['title']}")
print(f"  Biggest to-read book   : {long_unread[0]['title'] if long_unread else 'None'}")
print(f"  Reading progress       : {len(read_books)}/{len(books)} books")
print("=" * 62)

print("\n💡 CHALLENGE:")
print("  1. Write a function that recommends the next book to read by genre.")
print("  2. Add a 'date_read' field for completed books and sort by it.")
print("  3. Find the author with the most books in the library.")
print("  4. Create a 'wishlist.json' with books published after 2020.")
print()