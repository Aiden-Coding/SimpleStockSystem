from app.config import app
from app.job.stock_base_info_job import update_stock_base_infoT


@app.after_server_start
async def after_server_star(*_):
    # 启动定时任务
    await update_stock_base_infoT()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
    # 添加定时任务

# To Run:
# python run.py
