class book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def get_info(self):
    return f"Название книги: {self.title}\n" \
           f"Автор: {self.author}\n" \
           f"Год издания: {self.year}"

book1 = book("Гроза", "Александр Николаевич Островский", 1859)
print(book1.get_info())

