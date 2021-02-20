Class Article:

    def __init__(self,date,Author,publisher, wordcount):

        self.date = date
        self.Author = Author

    def find_Author(self):
      
       if self.Author == ' ':
          return 'no Author'
       else:
          return article.Author()

    def find_date(self):
      
      if self.date == ' '
        return 'no date'
      else:
        return self.date

   def find_publisher(self):
      
      if self.publisher == ' ':
        return 'no publisher'
      else:
          return self.publisher
       
  
def generate_articles(searched_news):
      
    if serched_news not a valid word:
        return 'no article'
    else:
        return 'results here!'


def find_keyword(keyword):
    
    if keyword not a valid word:
        return 'invalid'

    else:

        return 'results containing ' + keyword + ' here!'



def sort_by_date(articles):

    if articles not valid:
        return 'no articles'
    dates = []
    for article in articles:
        dates = dates + [getdate(article), article]
    sort dates
    return dates
        

def find_Articles_by(Author):

    count = 0
    if Author not a valid word:
        return 'no article'
    else:
        for articles written by Author:
            count += 1
        return count + ' articles written by ' + Author 
        


