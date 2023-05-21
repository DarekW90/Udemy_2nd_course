def BuyMe(prefix='pleases buy me', what='something nice', *args, **kwargs):
#def BuyMe(prefix='pleases buy me', what='something nice', *products):
    print(prefix, what)
    print(args)
    #print(products)
    print(kwargs)




BuyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop='market', color='any')

products = ['milk','bread','flakes']
parameters = {'price':'low','time':'now'}

BuyMe ('BuyMe', 'newspaper', *products, **parameters)