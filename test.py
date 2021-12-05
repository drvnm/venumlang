import requests
import asyncio
import aiohttp
from aiohttp_proxy import ProxyConnector, ProxyType
loop = asyncio.get_event_loop()

async def make_rqs():
        print("req begin")
        async with aiohttp.ClientSession() as session:

            r = await session.post(
            'http://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7032734350115047173&device_id=7025389329540040198&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220104&version_name=22.1.4&device_platform=android&ab_version=22.1.4&ssmix=a&device_type=G011A&device_brand=google&language=en&os_api=22&os_version=5.1.1&openudid=940f0062a04824b0&manifest_version_code=2022201040&resolution=1125*2436&dpi=375&update_version_code=2022201040&_rticket=1637437669639&app_type=normal&sys_region=US&mcc_mnc=31070&timezone_name=Asia%2FShanghai&ts=1637437660&timezone_offset=28800&build_number=22.1.4&region=US&carrier_region=US&uoo=0&app_language=en&locale=en&op_region=US&ac2=wifi&cdid=567a3c74-df10-4270-8ece-49efb0014cac&support_webview=1&okhttp_version=4.0.69.4-tiktok',
            proxy="http://161.129.152.226:3035",
            headers={
                "Host": "api22-normal-c-useast1a.tiktokv.com",
                "Cookie": "install_id=7032734350115047173; ttreq=1$88092a758dab1a37da11f2c2869dafdd040cf2bf; d_ticket=1355a02ad2202af73c65aff10c23c10ad74df; multi_sids=7030434437150327814%3A989bb465c9caf53b0adfb1f00d73ecd0; cmpl_token=AgQQAPNSF-RPsLGv8HijNh0_-x6rbCuS_4TZYMP09Q; odin_tt=3511c450ab56d1c88e0e96941b7eb6e41e0c0b248f2ad606c8277da8cb190eea0581f1a521a990e857984a8ec2b30a121c4e83bbceb4abd779637eb020d8df07ef4340a0df44e45945d6eccbb9ebcc0f; sid_guard=989bb465c9caf53b0adfb1f00d73ecd0%7C1637437517%7C5184000%7CWed%2C+19-Jan-2022+19%3A45%3A17+GMT; uid_tt=aa2ac5bb0774734ce909106978697f6152a990f8cbe274fabd0da31077fc2d31; sid_tt=989bb465c9caf53b0adfb1f00d73ecd0; sessionid=989bb465c9caf53b0adfb1f00d73ecd0; passport_csrf_token_default=72a3935b8a36bd3767fce35e6fad0338; store-idc=maliva; store-country-code=us",

                "X-Ss-Stub": "65AA4FC7117396AFA042A51D40623D3C",

                "Accept-Encoding": "gzip, deflate",

                "Passport-Sdk-Version": "19",

                "Sdk-Version": "2",

                "X-Tt-Multi-Sids": "7030434437150327814%3A989bb465c9caf53b0adfb1f00d73ecd0",

                "Multi_login": "1",

                "X-Tt-Token": "03989bb465c9caf53b0adfb1f00d73ecd003f534db3d279e6aab8b1c1246bb5d20bfbd06af9d5dbfddb8ff3dfacb967ebbd6d0328ffde4eb7c3926b7c5f482bc3c36bd5a5a69cb0b554cab3c63d2084f7cb433cfc9e2227dc8ba8c5666a5c8d786f5b-1.0.1",

                "X-Tt-Passport-Csrf-Token": "72a3935b8a36bd3767fce35e6fad0338",

                "X-Ss-Req-Ticket": "1637437669642",

            "X-Bd-Client-Key": "#hx8gGlOm96K2+LyPfupkiLEi3UZPCLSMRzAI0Y6NnVHn7ZwzD7BtO+X6vtJw8MBLPwGnv6n14szGjh7W",

                "X-Bd-Kmsv": "0",

                "X-Vc-Bdturing-Sdk-Version": "2.2.1.i18n",

                "X-Tt-Dm-Status": "login=1;ct=1;rt=1",

                "X-Tt-Cmpl-Token": "AgQQAPNSF-RPsLGv8HijNh0_-x6rbCuS_4TZYMP09Q",

                "X-Tt-Store-Idc": "maliva",

                "X-Tt-Store-Region": "us",

                "X-Tt-Store-Region-Src": "uid",

                "X-Tt-Store-Region-Did": "us",

                "X-Tt-Store-Region-Uid":"us",

                "User-Agent": "com.zhiliaoapp.musically/2022201040 (Linux; U; Android 5.1.1; en_US; G011A; Build/LMY48Z;tt-ok/3.10.0.2)",

                "X-Ladon":"05XNAsaw8SBl7YDwD29qXzSgK/uUfuEDB4qga1KnKKkvxmiC",

                "X-Khronos":"1637437669",

                "X-Gorgon": "0404805d400142ae89aff55fe319a6c5095de1e9797c549cc902",

                "X-Argus":"CTREREzFdMEVYoXFz3Ao5JluLV5DjLeVqWMzUxuOP9EE9CseK4j80JaChF72TZvGvZaSBTgWe3/3VY2YnMGxU/K37LE+E/rV16+C0jn5F//OAUmbE6t5YOeG9SFEgadQEIzMEW7+C/SQQsLkmE69fLrwlqQIYgnfRJK4LDYtR/h/MpQo4SiNVNUj+9aH9DqBGDlBcdYbUMG7U4GXejVGsI4Hceqy7MroW+JFwNT9uyXGwneEhxii6dUC4zOHchj3LQGzIeNr8ziV98w0C/jzzAYlwE29G2P74ogUL5vMTxW4LafTO+qGyaU8vBaOwuUSSzwQrSCn5paB5oT9KrVyVKs8tLsQvd30HkHKwqNEkIffDw==",

                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",

                "Content-Length": "51",
            },
            data=b"uid=7030434437150327814&login_name=cuze&page_from=0",
            
            )
            print(await r.text())
        print("req end")

async def main():
    while True:
        tasks = []
        for i in range(100):
            tasks.append(make_rqs())
        await asyncio.gather(*tasks)
    
loop.run_until_complete(main())