import requests      
import json


#url = ('https://newsapi.org/v2/everything?'
       #'q=rats&'
       #'from=2021-04-08&'
       #'sortBy=popularity&'
       #'apiKey=8aeba75069b44439b223e2cfa2d701d8')
#page = requests.get(main_url).json() 
  
#article = page["articles"] 

#results = [] 
      
#for ar in article: 
#    results.append(ar['title'] + ":" + ar['url']) 

#for i in range(len(results)): 
#    print(results[i].encode('utf-8')) 


def generate_articles(source):
    
    string = str(source)
    main_url = ('https://newsapi.org/v1/articles?'
             'source='+ str(source) + '&'
             'sortBy=top&'
             'apiKey=8aeba75069b44439b223e2cfa2d701d8')

    page = requests.get(main_url).json() 
    article = page["articles"] 
    results = [] 
    final = []
    for ar in article: 
        results.append(ar['title'] + " : " + ar['url'] + '\n') 
    #for i in range(len(results)): 
    #    print(results[i].encode('utf-8')) 
    #for ones in results:
    #    final.append[str(ones.encode('utf-8'))]

    return  str(results[0].encode('utf-8')) + '\n' + str(results[1].encode('utf-8')) + '\n' +  str(results[2].encode('utf-8')) + '\n' + str(results[3].encode('utf-8'))  + '\n' + str(results[4].encode('utf-8')) + '\n' + str(results[5].encode('utf-8')) + '\n' +  str(results[6].encode('utf-8')) + '\n' + str(results[7].encode('utf-8'))  + '\n' + str(results[8].encode('utf-8')) + '\n' + str(results[9].encode('utf-8'))      
  


def fool(text):

    return generate_articles(text)



#print(fool('the-verge'))






