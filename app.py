#!/usr/bin/python3

# Imports libs
from flask import Flask, jsonify, render_template
from lib_scrape import Scraper

# CONFIG DATA ----------------------------------------

# Polling interval
POLLING = 180000 # in ms. Default 3 min.

# Webpage data in the form of (short_name, weburl) per entry
WEBPAGES = [
    ('Best Buy PNY 3080','https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432655.p?skuId=6432655'),
    ('Newegg PNY 3080','https://www.newegg.com/pny-geforce-rtx-3080-vcg308010tfxppb/p/N82E16814133809?Description=VCG308010TFXPPB&cm_re=VCG308010TFXPPB-_-14-133-809-_-Product&quicklink=true'),
    ('B&H PNY 3080', 'https://www.bhphotovideo.com/c/product/1595985-REG/pny_technologies_vcg308010tfxppb_geforce_rtx_3080_10gb.html'),
    ('Amazon PNY 3080', 'https://www.amazon.com/dp/B08HBR7QBM'),
    ('Best Buy 3080 FE','https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440&ref=186&loc=nvidia_6429440'),
    ('Best Buy Test', 'https://www.bestbuy.com/site/yamaha-725w-4k-ultra-hd-5-1-channel-home-theater-system-with-bluetooth-black/6352589.p?skuId=6352589'),
    ('New Egg Test 1','https://www.newegg.com/asus-geforce-gtx-1660-super-dual-gtx1660s-o6g-evo/p/N82E16814126352'),
    ('New Egg Test 2','https://www.newegg.com/western-digital-2tb-black-sn850-nvme/p/N82E16820250160?Description=preorder&cm_re=preorder-_-20-250-160-_-Product'),
    ('B&H Test','https://www.bhphotovideo.com/c/product/1561080-REG/asus_tuf506ii_bs74_ryzen_7_4800h_8gb.html'),
    ('Amazon Test','https://www.amazon.com/Samsung-500GB-Internal-MZ-76E500B-AM/dp/B0781Z7Y3S/ref=sr_1_3?dchild=1&keywords=ssd&qid=1604181281&s=electronics&sr=1-3')
]

# Keyword data used to affirm stock
KEYWORDS = [
    # Best Buy
    'Add to Cart',
    'Get it today',
    # New Egg
    'Add to cart',
    'In stock',
    'PRE-ORDER',
    'Release Date',
    # B&H
    'Add to Cart',
    'Limited supply',
    'In Stock',
    # Amazon
    'In Stock',
    'Add to Cart',
    'Buy Now'
]

# ----------------------------------------------------

# Set app
app = Flask(__name__)

# Main page route
@app.route('/')
@app.route('/index')
def hello():
    webPages = []
    shortPage = [page[0] for page in WEBPAGES];
    longPage = [page[1] for page in WEBPAGES];
    for i in range (0,len(shortPage)):
        page = {
            'shortName': shortPage[i],
            'longName': longPage[i],
            'idName': shortPage[i].replace(' ', '_').replace('&','-')
        }
        webPages.append(page);
    return render_template('index.html', webPages=webPages, pollingInt=POLLING);

# Getter route for updates webpage info
@app.route('/update', methods=['POST'])
def update():

    # Run scrape
    shortPage = [page[0] for page in WEBPAGES];
    longPage = [page[1] for page in WEBPAGES];
    scraper = Scraper(shortPage, longPage, KEYWORDS);
    results = scraper.run_scrape();

    # Fix ampersand
    for key,value in results.items():
        if '&' in key:
            del results[key]
            results[key.replace('&','-')] = value

    return jsonify(results)



# Main
if __name__ == '__main__':
    
    # Load Scraper
    shortPage = [page[0] for page in WEBPAGES];
    longPage = [page[1] for page in WEBPAGES];
    scraper = Scraper(shortPage, longPage, KEYWORDS);

    print(scraper.run_scrape());

    # run app
    app.run(host='localhost', port=5000);