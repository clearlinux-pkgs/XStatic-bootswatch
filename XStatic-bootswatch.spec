#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-bootswatch
Version  : 3.3.7.0
Release  : 8
URL      : http://pypi.debian.net/XStatic-bootswatch/XStatic-bootswatch-3.3.7.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-bootswatch/XStatic-bootswatch-3.3.7.0.tar.gz
Summary  : bootswatch 3.3.7 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-bootswatch-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
XStatic-bootswatch
------------------
bootswatch javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-bootswatch package.
Group: Default
Provides: xstatic-bootswatch-python

%description python
python components for the XStatic-bootswatch package.


%prep
%setup -q -n XStatic-bootswatch-3.3.7.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487347816
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487347816
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
