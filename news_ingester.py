Class news_ingestor

  find()
  update()
  add()
  remove()
  wordcount()
  summerize()
  date()
  title()
  count()
  assign()
  enable_view()
  disable_view()
  Author()


def summarize(article):
    
    if article.wordcount <= 100
        return 'too short'
    else:
        return article.summerize()
        
        
def delete(news,text):
    
    if news does not exist:
        return 'news does not exist'
    elif text not in news:
        return 'text not in news'
    
    else:
        return news.remove(text)
    
def rename(news_article,new_title):
    
    if news_article does not exist:
        return 'no article'
         
    news_article.title() = new_title
    return news_article.title()



def generate_articles(searched_news):
      
    if serched_news not a valid word:
        return 'no article'
    else:
        return 'results here!'

def visibility(news,switch):
    
    if switch not in ['on','off']
        return 'invalid switch'
    elif switch in 'on':
        return news.enable_view()
    else:
        if switch in 'off':
            return news.disable_view()
        
def assign_Author(news,author):
    
    if news.Author() == ' ':
        news.Author == author
        return news.Author
    else:
        news.Author /= ' ':
            return 'has Author already' 
        
        
         
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
        


