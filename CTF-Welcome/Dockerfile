FROM golang:1-alpine AS builder

#Creating flag for the Challenge
RUN cd /home && mkdir Desktop 
RUN cd /home/Desktop && echo "CTF{Welcome_To_CTF_2021}" > - 

RUN apk add --no-cache git upx
RUN CGO_ENBALED=0 go get -ldflags '-w' github.com/yudai/gotty
RUN mv ${GOPATH}/bin/gotty /bin/ && \
        upx --brute /bin/gotty

FROM alpine:3.7

COPY --from=builder /bin/gotty /bin/gotty

ENTRYPOINT ["/bin/gotty"]