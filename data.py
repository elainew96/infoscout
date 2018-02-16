import pandas as pd
import operator

df = pd.read_csv("trips_gdrive.csv")

def retailer_affinity(focus_brand):
    iteration = 0
    retailer = {}
    for rows in df.iterrows():
        if(df.iloc[iteration][3]==focus_brand):
            store = df.iloc[iteration][2]
            try:
                retailer[store]+=df.iloc[iteration][6] #units sold
            except:
                retailer[store]=df.iloc[iteration][6]
        iteration = iteration + 1
    retailer = sorted(retailer.items(),key=operator.itemgetter(1),reverse=True)
    return retailer #returns tuples sortyed by the biggest retailer affinity

def count_hhs(brand=None, retailer=None, start_date = None, end_date=None):
    num_households = 0
    households = {}
    if (start_date == None):
        start_date = df.iloc[0][1]
    if (end_date == None):
        end_date = df.iloc[df.count][1]
    iteration = 0
    for rows in df.iterrows():
        if((df.iloc[iteration][1]>=start_date) and (df.iloc[iteration][1]<=end_date)):
            if ((df.iloc[iteration][3]==brand or brand==None)and
            (df.iloc[iteration][2]==retailer or retailer==None)):
                try:
                    households[df.iloc[iteration][4]]+=1 #increase what household bought more things
                except:
                    households[df.iloc[iteration][4]]=1
                    num_households+=1
            iteration+=1
    #    cannot do because csv is not sorted by dates (months are sorted, but not necessarily days)
    #    elif((df.iloc[iteration][1]>end_date)):
    #        break
        else:
            iteration+=1
            continue
    #could return households to see which household id did the most purchases
    return num_households

def top_buying_brand():
    brands = {}
    row = 0
    for rows in df.iterrows():
        try:
            brands[df.iloc[row][3]] += (int(df.iloc[row][5][1:])*int(df.iloc[row][6]))
        except:
            brands[df.iloc[row][3]] = (int(df.iloc[row][5][1:])*int(df.iloc[row][6]))
        row += 1
    brands = sorted(brands.items(),key=operator.itemgetter(1),reverse=True)
    return brands

if __name__ == '__main__':
    #print df.head(n=5)
    parent_brand = raw_input('Which brand would you like to see the biggest retailer affinity of? ')
    stuff = retailer_affinity(parent_brand)
    i = 1
    for values in stuff:
        print str(i) + '. ' + values[0] + ', ' + str(values[1]) + ' units sold'
        i += 1
    num = count_hhs(brand='Red Bull',start_date='1/2/2014',end_date='1/5/2014')
    print 'The number of households for the selected transaction is: ' +  str(num)

    i = 1
    print 'Top brands with most revenue:'
    top = top_buying_brand()
    for brands in top:
        print str(i) + '. ' + brands[0] + ': ' + str(brands[1])
        i+=1
