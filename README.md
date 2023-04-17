# Dynamic Plugin Service

## 动态插件服务

可根据需求定制插件接受数据推送并处理返回

### 使用方式

#### 定制消息接口

**API端点：/plugin/service**

**请求方式：POST**

在插件内定义好调用函数或方法，并放入plugins目录里，可参考demo.py

调用参数如下

```json
{
  "plugin": "demo",
  "method": "run_plugin",
  "data": 123
}
```

参数说明：

- plugin：插件名称
- method：插件调用入口方法
- data：入口参数

#### 原始消息接口

**API端点：/raw/service**

**请求方式：POST**

创建raw_开头的插件文件，放入plugins目录

插件需提供1个参数及2个方法

match_type 定义插件接受的请求体格式

check_data 方法实现请求数据的校验

run_plugin 方法实现插件的调用逻辑

可参考raw_demo.py

## 待实现功能

- [ ] 未识别原始数据入库及分析
- [ ] 完善GET请求触发功能点
- [ ] 接口认证需求梳理
- [ ] etc...
