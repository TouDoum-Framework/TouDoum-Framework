# Known issues

## Error when install psycopg2 on requirements.txt
Solution (Debian & Ubuntu)
```shell
apt install libpq-dev python3-dev
```

## Entrypoint.sh not working on linux
Solution : Convert entrypoint.sh to unix system
```shell
dos2unix entrypoint.sh
```