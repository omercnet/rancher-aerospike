FROM aerospike/aerospike-tools

RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/kennethreitz/requests/tarball/master && \
    tar zxfv master && \
    cd kennethreitz-requests* && \
    python setup.py install

COPY cluster_monitor.py /cluster_monitor.py

ENTRYPOINT /bin/bash
CMD ["python /cluster_monitor.py"]
