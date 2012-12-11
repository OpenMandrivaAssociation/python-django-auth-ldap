%define modname django-auth-ldap
%define name    python-%{modname}
%define version 1.1
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Django LDAP authentication backend
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/django-auth-ldap/
Source0: 	http://pypi.python.org/packages/source/d/django-auth-ldap/django-auth-ldap-%{version}.tar.gz
BuildRequires:	    python-devel
Requires:	    python-django
Requires:	    python-ldap

%description
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

%prep
%setup -q -n %modname-%version

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc docs/*
%{python_sitelib}/django_auth_ldap
%{python_sitelib}/django_auth_ldap-%{version}-py*.egg-info


%changelog
* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1mdv2012.0
+ Revision: 799702
- version update 1.1

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-1
+ Revision: 688438
- update to new version 1.0.10

* Mon Mar 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.9-1
+ Revision: 648672
- update to new version 1.0.9

* Thu Mar 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8-1
+ Revision: 646101
- update to new version 1.0.8

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 622931
- update to new version 1.0.7

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.0.6-2mdv2011.0
+ Revision: 592243
- rebuild for python 2.7

* Fri Jul 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 563453
- update to new version 1.0.6

* Mon Jul 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 554938
- import python-django-auth-ldap

