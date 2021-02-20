from news_ingester import *

define test_news():
  
  assert summarize('this is news', 4) == 'too short'
  assert summarize('this is news', 1) == 'summarized'
  assert delete('this is news','is' == 'this    news'
  assert delete(jkl,'k') == 'invalid news/text'
  assert delete('jkl',k) == 'invalid news/text'
  assert delete('jkl','a') == 'text not in news'
  assert rename('title1','title2') == 'title updated'
  assert rename('title1','title1') == 'title unchanged'
  assert rename(title1,'title2') == 'invalid title'
  assert rename('title1',title2) == 'invalid title'
  assert generate_artices(article) == 'no articles found'
  assert generate_article('article') == 'results here:'
  assert visibilty(news,'on') == 'view enabled'
  assert visibility(news,'off') == 'view disabled'
  assert visibility(news,k) == 'invalid switch'
  assert assign_Author(news,author1) == 'has Author already'
  assert assign_Author(news,author2) == 'Author updated'
  
