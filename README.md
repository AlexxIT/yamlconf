# Store app config in yaml file

```yaml
logging:
  formatters:
    stream: {format: "%(asctime)s %(levelname)s [%(name)s] %(message)s"}
    syslog: {format: "%(asctime)s %(name)s python: %(message)s"}
  handlers:
    stream:
      class: logging.handlers.SysLogHandler
      stream: ext://sys.stdout
      formatter: stream
    syslog:
      class: logging.handlers.SysLogHandler
      address: ['127.0.0.1', 5140]
      formatter: syslog
  loggers:
    asyncio: {level: WARNING}
    urllib3.connectionpool: {level: INFO}
    websockets.protocol: {level: WARNING}
  root:
    level: DEBUG
    handlers: [stream, syslog]

server:
  user: ...
  pass: ...
```

OR

```yaml
logging:
  filename: "app.log"
  datefmt: "[%Y-%m-%d %H:%M:%S %z]"
  format: "%(asctime)s %(levelname)s [%(name)s] %(message)s"
  level: DEBUG
  
server:
  user: ...
  pass: ...
```

# Changelog

## 0.1.2 - 2019-04-05

- Add `basicConfig` version

## 0.1.1 - 2019-04-01

- Fix empty logging in conf