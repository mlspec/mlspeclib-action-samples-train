FROM mlspec/mlspeclib-action-docker@sha256:12f9f4a95c9cf4f3fd7e20313c164cb699944bcf753e4f71aa326538999d749b

RUN apt-get -y update && apt-get -y install python3-all python3-pip

COPY requirements.txt /requirements.txt

ARG FIRSTCACHEBUST=1

RUN python3 -m pip install -U pip
RUN python3 -m pip install --no-cache-dir -r /requirements.txt

COPY .parameters/schemas /src/parameters
COPY integration/.parameters/schemas /src/parameters/test_schemas
COPY step_execution.py /src

ENTRYPOINT ["./entrypoint.sh"]
