REPO := fragmentedcurve
DEPS := quakelive-server
SERVERS := quakelive-ca quakelive-actf quakelive-overkill

.PHONY: all $(SERVERS)

all: $(SERVERS)

$(DEPS):
	docker build -f Dockerfiles/Dockerfile.$@ -t $@ .

$(SERVERS): $(DEPS)
	docker build -f Dockerfiles/Dockerfile.$@ -t $(REPO)/$@ .

