Name:           hidl-audio-FP4
Version:        0.1
Release:        0
License:        MIT
Summary:        Hidl compatible audio driver for FP4
Provides: 	libaudiohal
Requires:	pulseaudio-modules-droid
AutoReq: 	no

%description
This driver provides shared libraries needed by pulseaudio.

%install
mkdir -p $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/lib64/hw/
cp $ANDROID_ROOT/hybris/mw/hidl_audio/binaries/audio.hidl_compat.default.so $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/lib64/hw/audio.hidl_compat.default.so
ln -s /apex/com.android.vndk.v30/lib64/libaudioroute.so $RPM_BUILD_ROOT/usr/libexec/droid-hybris/system/lib64/libaudioroute.so

%files
/usr/libexec/droid-hybris/system/lib64/libaudioroute.so
/usr/libexec/droid-hybris/system/lib64/hw/audio.hidl_compat.default.so


%changelog
# Initial version

