# API contracts

Workstreams build against this file. Changing it requires a pull request labelled `contract-change`.

## GET /health

WS-2 owns this route. Anyone may call it.

```http
GET /health
200 application/json
{ "status": "ok" }
```

## MeterReading

WS-3 produces this payload, WS-2 serves it, and WS-1 displays it. Example schema — replace it with the real contract before another workstream depends on it.

```text
MeterReading {
  id: string
  timestamp: string    # ISO-8601
  value: number
  unit: string         # e.g. "kWh"
}
```
