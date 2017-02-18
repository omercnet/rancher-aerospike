FROM aerospike/aerospike-server

COPY aerospike.conf /etc/aerospike/aerospike.conf.template
COPY configure.py /configure.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["asd"]
