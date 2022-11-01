import asyncio

colors = {'Red': 'Green',
          'Yellow': 'Red',
          'Green': 'Red'
          }


async def change_color(i):
    color = ''

    if 0 <= i < 4:
        color = 'Red'
    elif 4 <= i < 6 or 10 <= i < 12:
        color = 'Yellow'
    elif 6 <= i < 10:
        color = 'Green'
    print(color.ljust(8), colors[color].ljust(8))
    return


async def main():
    while True:
        for i in range(12):
            await change_color(i)
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
