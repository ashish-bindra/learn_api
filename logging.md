# Logging

## `logger.bind()`

- It is used to attach extra contextual information to log message
- Every log generated through bound logger came the same context

```
logger
  |----- txnid
           |-----> service-1 
           |-----> service-2
```

when you have many services, thread or analsis task

eg1

```py
log1 = logger.bind(txnid='123')
log2 = logger.bind(txnid='456')

log1.info("Request1")
log2.info("Request2")
```
