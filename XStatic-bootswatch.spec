#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-bootswatch
Version  : 3.3.5.3
Release  : 5
URL      : https://pypi.python.org/packages/source/X/XStatic-bootswatch/XStatic-bootswatch-3.3.5.3.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-bootswatch/XStatic-bootswatch-3.3.5.3.tar.gz
Summary  : bootswatch 3.3.5 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-bootswatch-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
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
%setup -q -n XStatic-bootswatch-3.3.5.3

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
