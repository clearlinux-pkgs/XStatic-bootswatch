#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-bootswatch
Version  : 3.3.7.0
Release  : 11
URL      : http://pypi.debian.net/XStatic-bootswatch/XStatic-bootswatch-3.3.7.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-bootswatch/XStatic-bootswatch-3.3.7.0.tar.gz
Summary  : bootswatch 3.3.7 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-bootswatch-python3
Requires: XStatic-bootswatch-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
XStatic-bootswatch
        ------------------
        
        bootswatch javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package
        `XStatic`.

%package python
Summary: python components for the XStatic-bootswatch package.
Group: Default
Requires: XStatic-bootswatch-python3
Provides: xstatic-bootswatch-python

%description python
python components for the XStatic-bootswatch package.


%package python3
Summary: python3 components for the XStatic-bootswatch package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-bootswatch package.


%prep
%setup -q -n XStatic-bootswatch-3.3.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532215604
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
