# Dynamic Plugin Service

## 动态插件服务

可根据需求定制插件接受数据推送并处理返回

### 使用方式

在插件内定义好调用函数或方法，并放入plugins目录里

通过post请求api端点 /plugin/service

调用参数如下

```json
{
    "plugin":"plugin1", //插件名称
    "method":"run_plugin", //插件调用入口方法
    "data":123 //入口参数
}
```

