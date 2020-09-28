REPO := fragmentedcurve
DEPS := quakelive-server
SERVERS := quakelive-ca quakelive-actf

.PHONY: all $(SERVERS)

all: $(SERVERS)

$(DEPS):
	docker build -f Dockerfiles/Dockerfile.$@ -t $@ .

$(SERVERS): $(DEPS)
	docker build -f Dockerfiles/Dockerfile.$@ -t $(REPO)/$@ .

