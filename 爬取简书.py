import requests, lxml
from bs4 import BeautifulSoup

'''
每次点击简书主页，会发现其推荐的文章是不听变化的，
但不管怎么变化，只要拿到超链接，通过文章超链接的到文章的文本和图片是可以的
缺点就是每次爬取的文章都不同，所以文本和图片也不同
'''

main_url = "https://www.jianshu.com"
newslist = []    #存放文章url
picture = []    #存放图片url
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
#获取文章链接模块
def get_a(url, arr ,headers = headers):
    r = requests.get(url, headers = headers)
    content = r.text
    soup = BeautifulSoup(content,"lxml")
    image_soups = soup.select(".index .main #list-container .content .title")
    for image_soup in image_soups:
        newslist.append("https://www.jianshu.com" + image_soup['href'])
    return newslist

#保存文章链接模块
def save_text(arr1, headers = headers):
    for i in range(len(arr1)):
        r1 = arr1[i]
        print(arr1[i])
        text_r = requests.get(r1,headers = headers )
        content_p = text_r.text
        soup_p = BeautifulSoup(content_p, "lxml")
        #text_ps = soup_p.find_all(class_ = "show-content-free")
        text_ps = soup_p.select(".show-content-free p")
        for text_p in text_ps:
            str1 = text_p.text+"\n"
            file = open("C:\\Users\\del\\Desktop\\picture\\{}.txt".format(i),"a",encoding="utf-8")
            file.write(str1)
            file.close()

#保存文章图片模块
def save_pic(arr1,arr2, headers = headers):
    for i in range(len(arr1)):
        r1 = arr1[i]
        print(arr1[i])
        img_r = requests.get(r1,headers = headers )
        content_p = img_r.text
        soup_img = BeautifulSoup(content_p, "lxml")
        pic_imgs = soup_img.select(".show-content .show-content-free .image-package .image-view img")
        for pic_img in pic_imgs:
            arr2.append("https:" + pic_img["data-original-src"])
            #print(arr2)
            for index, url in enumerate(arr2):
                r = requests.get(url, headers=headers)
                with open("C:\\Users\\del\\Desktop\\picture\\{}.jpg".format(index), "wb") as file:
                    file.write(r.content)
        print(arr2)
#执行模块
def strat(url):
    text_list = get_a(url,newslist)
    save_text(text_list)
    save_pic(text_list,picture)


if __name__ == "__main__":
    strat(main_url)


