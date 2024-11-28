def extract_books(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    
    books = []
    book_entries = data.strip().split("\n\n")  # Split each book entry by double newlines
    for entry in book_entries:
        lines = entry.split("\n")
        title = lines[0].strip()
        subtitle = None
        author = None
        format_ = "Book"  # Default to 'Book'
        
        if len(lines) > 1:
            # Handle subtitles and author lines
            if lines[1].strip().startswith("by "):  # No subtitle, author directly
                author_line = lines[1].strip()
            else:
                subtitle = lines[1].strip()
                author_line = lines[2].strip() if len(lines) > 2 else ""
            
            # Detect format (e.g., Graphic Novel, Book, etc.)
            for line in lines:
                if "Graphic Novel" in line:
                    format_ = "Graphic Novel"
                elif "Book" in line:
                    format_ = "Book"
                elif "|" in line:  # Handle language notes, e.g., "Book - 2023 | Spanish"
                    format_ = line.split("|")[0].strip()

        # Extract author from the line
        author_match = re.search(r"by (.+)", author_line)
        if author_match:
            author = author_match.group(1)
        else:
            print(f"Warning: Could not find author for entry:\n{entry}\n")
        
        # Append extracted details to books list
        books.append({
            "title": title,
            "subtitle": subtitle,
            "author": author,
            "format": format_,
        })
    return books
