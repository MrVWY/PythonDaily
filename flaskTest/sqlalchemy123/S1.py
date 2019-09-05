from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy123.models import Users

engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/180",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

Session = sessionmaker(bind=engine)
session = Session()

obj = Users(name='ZJH',age=18,email='123163com')
session.add(obj)

#提交事务
session.commit()
#关闭session
session.close()