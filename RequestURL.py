import requests

while True:
    url = input("请输入url(或者按'q'退出)\n")
    if url == "q":
        break
    if not url:
        url = "https://www.baidu.com"
        print("使用默认url")
    elif not url.startswith("http://" and "https://"):
        url = "https://" + url

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("成功:", response.status_code)
        print("延迟:", response.elapsed.total_seconds() * 100, "ms")

    except requests.exceptions.Timeout:
        print("超时(GFW)")
    except requests.exceptions.SSLError:
        print("SSL错误")
    except requests.exceptions.RequestException as e:
        print(f"失败: {e}")
