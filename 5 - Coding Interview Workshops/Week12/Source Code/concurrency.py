import asyncio
import aiohttp
import time
import multiprocessing
import matplotlib.pyplot as plt
import requests

BASE_URL = 'https://animechan.xyz/api/random'

async def make_request(session):
    async with session.get(BASE_URL) as response:
        if response.content_type == 'application/json':
            return await response.json()
        else:
            return await response.text()

async def async_task(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.ensure_future(make_request(session))
            tasks.append(task)
        await asyncio.gather(*tasks)

def sync_task(num_requests):
    for _ in range(num_requests):
        requests.get(BASE_URL)

def make_request_sync(_):
    return requests.get(BASE_URL)

def multiprocessing_task(num_requests):
    with multiprocessing.Pool() as pool:
        pool.map(make_request_sync, range(num_requests))

def main():
    num_requests_list = [10, 20, 30, 40, 50]
    sync_times = []
    async_times = []
    multiprocessing_times = []

    for num_requests in num_requests_list:
        start_time = time.time()
        sync_task(num_requests)
        end_time = time.time()
        sync_times.append(end_time - start_time)

        start_time = time.time()
        asyncio.run(async_task(num_requests))
        end_time = time.time()
        async_times.append(end_time - start_time)

        start_time = time.time()
        multiprocessing_task(num_requests)
        end_time = time.time()
        multiprocessing_times.append(end_time - start_time)

    plt.plot(num_requests_list, sync_times, label="Synchronous")
    plt.plot(num_requests_list, async_times, label="Asyncio")
    plt.plot(num_requests_list, multiprocessing_times, label="Multiprocessing")
    plt.xlabel("Number of Requests")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Comparison")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()