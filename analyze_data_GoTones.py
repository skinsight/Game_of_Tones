import operator

def update_items_sold_count(items_sold_count, pd_series):
    #Update count for each product sold YTD
    items = pd_series.value_counts().index.tolist()
    item_counts = pd_series.value_counts().tolist()
    for item_idx, item in enumerate(items):
        #print(item)
        if item in items_sold_count:            
            items_sold_count[item] = items_sold_count[item] + item_counts[item_idx]
        else:
            items_sold_count[item] = item_counts[item_idx]
    return items_sold_count


def get_complimentary_gifts(df):
    #Get most purchased product YTD for each customer and then print using .format() to inform fulfillment team
    clients = df.columns[1:]
    for client in clients:
        item_bght_most_freq = df[client].value_counts().index.tolist()[0]
        print("Send {} a complimentary {}".format(client, item_bght_most_freq))

        
def get_product_perf(df):
    #Get count for each product sold YTD
    clients = df.columns[1:]
    items_sold_count = dict()
    for client in clients:
        items_sold_count = update_items_sold_count(items_sold_count, df[client])
    return items_sold_count


def get_best_perf_prod(items_sold_count):
    best_perf_prod = max(items_sold_count.items(), key=operator.itemgetter(1))[0]
    print('Highest-performing product is: {}'.format(best_perf_prod))

def get_worst_perf_prod(items_sold_count):
    worst_perf_prod = min(items_sold_count.items(), key=operator.itemgetter(1))[0]
    print('Lowest-performing product is: {}'.format(worst_perf_prod))