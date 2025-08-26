ARG BUILD_FROM=ghcr.io/hassio-addons/base:18.1.0

FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    wireguard-tools \
    openssh \
    rsync \
    nano \
    jq \
    nftables \
    coreutils

COPY rootfs /
