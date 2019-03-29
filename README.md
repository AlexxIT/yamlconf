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