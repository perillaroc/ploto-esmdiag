# Ploto-esmdiag

An extension for esmdiag. Including:

- A fetcher to retrieval data from EDP (earth data platform)
- A plotter embedded NCL scripts from [dongli/esmdiag](https://github.com/dongli/esmdiag) project.
- A processor embedded data operations used by [dongli/esmdiag](https://github.com/dongli/esmdiag) project.

## Docker

Build `nwpc-oper/ploto-esmdiag:base` image.

```bash
docker build --rm --tag nwpc-oper/ploto-esmdiag:base --file docker/base/Dockerfile .
```

Build `nwpc-oper/plot-esmdiag:consumer` image.

```bash
docker build --rm --tag nwpc-oper/plot-esmdiag:consumer --file docker/consumer/Dockerfile .
```

## LICENSE

Copyright 2020, perillaroc at nwpc-oper.

`ploto-esmdiag` is licensed under [GPL-3.0](./LICENSE.md).

Components named `esmdiag` and files under `vendor/esmdiag` are
based on [dongli/esmdiag](https://github.com/dongli/esmdiag).