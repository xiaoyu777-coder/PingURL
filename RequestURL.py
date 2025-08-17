import requests
from decimal import Decimal as Dec

while True:
    # 获取用户输入的URL，或者按'q'退出
    url = input("请输入url(或者输入'q'退出)\n")
    if url == "q":
        break
    # 如果用户没有输入URL，则使用默认的URL
    if not url:
        url = "https://www.baidu.com"
        print("使用默认url")
    # 如果URL不是以 "http://" 或 "https://" 开头，则添加 "https://"
    elif not url.startswith("http://" and "https://"):
        url = "https://" + url

    # 设置请求头，模拟浏览器访问
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    try:
        # 禁用urllib3的警告，忽略SSL证书验证错误
        requests.packages.urllib3.disable_warnings()
        # 发送GET请求，设置5秒超时
        response = requests.get(url, headers=headers, timeout=5, verify=False)
        # 如果请求失败（状态码不是2xx），则抛出异常
        response.raise_for_status()
        # 打印成功状态码和延迟（毫秒）
        print("成功:", response.status_code)
        print("延迟:", Dec(response.elapsed.total_seconds() * 100).quantize(Dec("0.00")), "ms")

    except requests.exceptions.Timeout:
        # 捕获超时异常
        print("超时(GFW)")
    except requests.exceptions.ConnectionError:
        # 捕获域名解析失败异常
        print("域名解析失败")
    except requests.exceptions.RequestException as e:
        # 捕获其他请求异常
        print(f"失败: {e}")