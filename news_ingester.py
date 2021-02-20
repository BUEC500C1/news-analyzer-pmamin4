Class news_ingestor

  find()
  update()
  add()
  remove()
  wordcount()
  summarize()
  date()
  title()
  count()
  assign()
  enable_view()
  disable_view()
  Author()


def summarize(news,limit):
    
    if news.wordcount <= limit
        return 'too short'
    else:
        news.summarize
        return 'summarized'
        
        
        
def delete(news,text):
    
    if news is not str():
        return 'invalid news/text'
      
    elif text is not str():
        return 'invalid news/text'
      
    elif text not in news:
        return 'text not in news'
    
    else:
        return news.remove(text)
    
def rename(news_article,new_title):
    
    if news_article.title() == new_title:
        return 'title unchanged'
    elif news_article is not str():
      return 'invalid title'
    elif new_title is not str():
      return 'invalid title'
    else:
      news_article.title() = new_title
      return 'title updated'



def generate_articles(searched_news):
      
    if serched_news is not str():
        return 'no articles found'
    else:
        return 'results here:'

def visibility(news,switch):
    
    if switch not in ['on','off']
        return 'invalid switch'
    elif switch in 'on':
        news.enable_view()
        return 'view enabled'
    else:
        if switch in 'off':
            news.disable_view()
            return 'view disabled'
        
def assign_Author(news,author):
    
    if news.Author() == ' ':
        news.Author == author
        return 'Author updated'
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
        


