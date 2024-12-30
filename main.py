from tqdm import tqdm
from function.search import Search
from function.detail import Detail
from utils.spider_config import spider_config
d = Detail()
s = Search()
def get_search_url(cur_page, city_id, keyword='炸鸡'):
    """
    获取搜索链接
    @param cur_page: 当前页码
    @param city_id: 城市ID
    @param keyword: 搜索关键字
    @return: 拼接好的搜索URL和一些需要的选项
    """
    # 使用简单的字符串拼接构建URL
    base_url = 'http://www.dianping.com/search/keyword/' + city_id + '/0_' + keyword + '/p'

    # 根据页码构建搜索URL
    if cur_page == 1:
        return base_url + "1", 'proxy, cookie'
    else:
        return base_url + str(cur_page), 'proxy, cookie'

for page in tqdm(range(1, spider_config.NEED_SEARCH_PAGES+1), desc='搜索页数'):
    search_url, request_type = get_search_url(page, spider_config.LOCATION_ID,spider_config.KEYWORD)
    search_res = s.search(search_url, request_type)
    if not search_res:
        break
    print(search_res)
    for each_search_res in tqdm(search_res, desc='详细爬取'):
        # 爬取推荐菜
        shop_id = each_search_res['店铺id']

        each_detail_res = d.get_detail(shop_id)
        each_search_res.update(each_detail_res)
        print(each_search_res)

    if len(search_res) < 15:
        break

# all_data=[]
# for page in range(1, spider_config.NEED_SEARCH_PAGES + 1):
#     search_url, request_type = get_search_url(page, spider_config.LOCATION_ID, spider_config.KEYWORD)
#     search_res = s.search(search_url, request_type)
#
#     if not search_res:
#         break
#
#     all_data.extend(search_res)  # 添加当前页的所有店铺数据到总列表中
#
#     if len(search_res) < 15:
#         break
# print(all_data)