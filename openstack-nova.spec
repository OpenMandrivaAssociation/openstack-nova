%global with_doc 1

%define bzr_rev 786
Name:             openstack-nova
Version:          2011.1.%{bzr_rev}
Release:          %mkrel 1
Summary:          OpenStack Compute (nova) current bzr snapshot
Group:            Development/Other
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
# download latest snapshot from
# http://hudson.openstack.org/job/nova-tarball/lastSuccessfulBuild/artifact/dist/<tarball>
# then bznew the tar.gz
Source0:          nova-2011.2~bzr%{bzr_rev}.tar.bz2
Source1:          nova.conf
Source9:          %{name}.logrotate
Source10:         %{name}-sudoers
Source11:         %{name}.init
Patch1:           openstack-nova-2011.1-default-configfile.diff
BuildRoot:        %{_tmppath}/nova-%{version}-%{release}-root-%(%{__id_u} -n)

%define sharedstatedir %{_localstatedir}/lib

BuildRequires:    python-devel
BuildRequires:    python-setuptools
BuildRequires:    python-distutils-extra
BuildRequires:    python-netaddr
BuildRequires:    python-pyxml
BuildRequires:    fdupes intltool
Requires:         python-nova = %{version}-%{release}
Requires:         sudo euca2ools logrotate
Requires(pre):    shadow-utils

%description
ATTENTION! This is a development snapshot, handle with care!

Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

Nova is intended to be easy to extend, and adapt. For example, it currently
uses an LDAP server for users and groups, but also includes a fake LDAP server,
that stores data in Redis. It has extensive test coverage, and uses the Sphinx
toolkit (the same as Python itself) for code and user documentation.

%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         PyXML
Requires:         curl
# actually, libvirt requires ebtables for the stuff we want to do with it.
# for "standard" applications, libvirt runs fine without ebtables, so add the
# dependency here.
Requires:         ebtables
Requires:         python-m2crypto
Requires:         python-ipy
Requires:         python-boto
Requires:         python-carrot
Requires:         python-cheetah
Requires:         python-daemon <= 1.5.5
Requires:         python-eventlet
Requires:         python-gflags
Requires:         python-mox
Requires:         python-redis >= 2.0
Requires:         python-routes
Requires:         python-sqlalchemy >= 0.6
Requires:         python-sqlalchemy-migrate >= 0.6
Requires:         python-tornado
Requires:         python-twisted
Requires:         python-webob
Requires:         python-netaddr

%description -n   python-nova
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} Python library.

%package          ajax-console-proxy
Summary:          Ajax Console Proxy Server
Group:            Applications/System

Requires:         %{name} = %{version}-%{release}

%description      ajax-console-proxy
A method to interact with Virtual Machines that works even when the VM's network is dead.
The ajax-console-proxy will allow users to interact with instances that would otherwise
be rendered impossible to fix without assistance from cloud providers staff. 

This package contains the %{name} ajax console proxy server.

%package          api
Summary:          A nova api server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}
Requires:         redis
Recommends:       python-mysql
Recommends:       python-sqlite2

%description      api
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} api server.

%package          compute
Summary:          A nova compute server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}
Requires:         libvirt-python >= 0.8.1
Requires:         libxml2-python
Requires:         python-glance

%description      compute
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} compute server.

%package          instancemonitor
Summary:          A nova instancemonitor server
Group:            Applications/System

Requires:         %{name} = %{version}-%{release}

%description      instancemonitor
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} instance monitor.

%package          network
Summary:          A nova network server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}
Requires:         python-netifaces tunctl

%description      network
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} network server.

%package          objectstore
Summary:          A nova objectstore server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}

%description      objectstore
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} object store server.

%package          scheduler
Summary:          A nova scheduler server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}

%description      scheduler
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} scheduler server.

%package          volume
Summary:          A nova volume server
Group:            Applications/System
Requires:         %{name} = %{version}-%{release}
Requires:         aoetools
#Requires:         vblade-persist

%description      volume
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} volume server.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for %{name}
Group:            Documentation
BuildRequires:    python-sphinx
# Required to build module documents
BuildRequires:    python-ipy
BuildRequires:    python-boto
BuildRequires:    python-carrot
BuildRequires:    python-cheetah
BuildRequires:    python-daemon 
BuildRequires:    python-eventlet
BuildRequires:    python-gflags
BuildRequires:    python-glance
BuildRequires:    python-m2crypto
BuildRequires:    python-mox
BuildRequires:    python-pyrrd
BuildRequires:    python-redis
BuildRequires:    python-routes
BuildRequires:    python-sqlalchemy
BuildRequires:    python-sqlalchemy-migrate
BuildRequires:    python-tornado
BuildRequires:    python-twisted
BuildRequires:    python-webob

%description      doc
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains documentation files for %{name}.
%endif

%prep
%setup -q -n nova-2011.2 #%%{version}
%patch1 -p1

%build
%{__python} setup.py build


%install
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

# make rpmlint happy :-)
gzip -9 ChangeLog

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

rm %{buildroot}/usr/share/doc/nova/README

# Setup directories
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -d -m 755 %{buildroot}%{sharedstatedir}/nova
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{sharedstatedir}/nova/monitor
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova
cp -rp CA %{buildroot}%{sharedstatedir}/nova
# the code seems broken, so we need a symlink...
ln -s %{sharedstatedir}/nova/CA %{buildroot}%{python_sitelib}

# Install init files
mkdir -p %{buildroot}%{_initrddir}
for i in api compute network objectstore scheduler volume instancemonitor ajax-console-proxy
do
    tmp=$(mktemp)
    cat %{SOURCE11} | sed "s/__NAME__/$i/g" > $tmp
    install -m 755 $tmp %{buildroot}%{_initrddir}/%{name}-$i
done

# Install sudoers
#install -p -D -m 440 %{SOURCE10} %{buildroot}%{_sysconfdir}/sudoers.d/%{name}

# Install logrotate
install -p -D -m 644 %{SOURCE9} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install config files
install -p -D -m 644 %{SOURCE1}		%{buildroot}%{_sysconfdir}/nova/nova.conf
mv %{buildroot}%{_sysconfdir}/api-paste.ini	%{buildroot}%{_sysconfdir}/nova/api-paste.ini


# Install template files
install -p -D -m 644 nova/auth/novarc.template %{buildroot}%{_datadir}/nova/novarc.template
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datadir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/libvirt.xml.template %{buildroot}%{_datadir}/nova/libvirt.xml.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datadir}/nova/interfaces.template

# Install pid directory  
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova  

# Install euca-get-ajax-console
install -p -D -m 755 tools/euca-get-ajax-console %{buildroot}%{_bindir}/euca-get-ajax-console

# Install Ajaxterm
# FIXME: nova-compute looks up the ajaxterm at the moment in %{python_sitelib}/tools, should be moved to some other place
install -d -m 755 %{buildroot}%{python_sitelib}/tools/ajaxterm
install -p -D -m 644 tools/ajaxterm/ajaxterm.css %{buildroot}%{python_sitelib}/tools/ajaxterm/ajaxterm.css
install -p -D -m 644 tools/ajaxterm/ajaxterm.html %{buildroot}%{python_sitelib}/tools/ajaxterm/ajaxterm.html
install -p -D -m 644 tools/ajaxterm/ajaxterm.js %{buildroot}%{python_sitelib}/tools/ajaxterm/ajaxterm.js
install -p -D -m 644 tools/ajaxterm/qweb.py %{buildroot}%{python_sitelib}/tools/ajaxterm/qweb.py
install -p -D -m 644 tools/ajaxterm/sarissa_dhtml.js %{buildroot}%{python_sitelib}/tools/ajaxterm/sarissa_dhtml.js
install -p -D -m 644 tools/ajaxterm/sarissa.js %{buildroot}%{python_sitelib}/tools/ajaxterm/sarissa.js
install -p -D -m 755 tools/ajaxterm/ajaxterm.py %{buildroot}%{python_sitelib}/tools/ajaxterm/ajaxterm.py

# Clean CA directory
find %{buildroot}%{sharedstatedir}/nova/CA -name .gitignore -delete
find %{buildroot}%{sharedstatedir}/nova/CA -name .placeholder -delete

fdupes %{buildroot}%{python_sitelib}/nova

%clean
rm -rf %{buildroot}

%pre
getent group nova >/dev/null || groupadd -r nova
getent passwd nova >/dev/null || \
useradd -r -g nova -d %{sharedstatedir}/nova -s /sbin/nologin \
-c "OpenStack Nova Daemons" nova
exit 0

%post ajax-console-proxy
%fillup_and_insserv -f -y openstack-nova-ajax-console-proxy

%preun ajax-console-proxy
%stop_on_removal openstack-nova-ajax-console-proxy

%post api
%fillup_and_insserv -f -y openstack-nova-api

%preun api
%stop_on_removal openstack-nova-api

%post compute
%fillup_and_insserv -f -y openstack-nova-compute

%preun compute
%stop_on_removal openstack-nova-compute

%post instancemonitor
%fillup_and_insserv -f -y openstack-nova-instancemonitor

%preun instancemonitor
%stop_on_removal openstack-nova-instancemonitor

%post network
%fillup_and_insserv -f -y openstack-nova-network

%preun network
%stop_on_removal openstack-nova-network

%post objectstore
%fillup_and_insserv -f -y openstack-nova-objectstore

%preun objectstore
%stop_on_removal openstack-nova-objectstore

%post scheduler
%fillup_and_insserv -f -y openstack-nova-scheduler

%preun scheduler
%stop_on_removal openstack-nova-scheduler

%post volume
%fillup_and_insserv -f -y openstack-nova-volume

%preun volume
%stop_on_removal openstack-nova-volume

%postun
%insserv_cleanup

%files
%defattr(-,root,root,-)
%doc README ChangeLog.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/nova/nova.conf
#%config(noreplace) %{_sysconfdir}/sudoers.d/%{name}
%dir %{_sysconfdir}/nova
%dir %attr(0755, nova, root) %{_localstatedir}/log/nova 
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova
%{_bindir}/nova-manage
%{_bindir}/nova-debug
%{_bindir}/nova-logspool
%{_bindir}/nova-spoolsentry
%{_bindir}/nova-console
%{_bindir}/nova-direct-api
%{_bindir}/stack
%defattr(-,nova,nobody,-)
%dir %{sharedstatedir}/nova
%{sharedstatedir}/nova/*
%{_datadir}/*
%{python_sitelib}/CA
%{_mandir}/man1/ajaxterm.1*

%files -n python-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/run_tests.py*
##%{python_sitelib}/nova-%{version}-*.egg-info
%{python_sitelib}/nova-*-*.egg-info

%files api
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/nova/api-paste.ini
%{_initrddir}/%{name}-api
%{_bindir}/nova-api

%files compute
%defattr(-,root,root,-)
%{_bindir}/nova-compute
%{_initrddir}/%{name}-compute
%dir %{python_sitelib}/tools
%dir %{python_sitelib}/tools/ajaxterm
%{python_sitelib}/tools/ajaxterm/*

%files ajax-console-proxy
%defattr(-,root,root,-)
%{_bindir}/nova-ajax-console-proxy
%{_bindir}/euca-get-ajax-console
%{_initrddir}/%{name}-ajax-console-proxy

%files instancemonitor
%defattr(-,root,root,-)
%{_bindir}/nova-instancemonitor
%{_initrddir}/%{name}-instancemonitor

%files network
%defattr(-,root,root,-)
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_initrddir}/%{name}-network

%files objectstore
%defattr(-,root,root,-)
%{_bindir}/nova-import-canonical-imagestore
%{_bindir}/nova-objectstore
%{_initrddir}/%{name}-objectstore

%files scheduler
%defattr(-,root,root,-)
%{_bindir}/nova-scheduler
%{_initrddir}/%{name}-scheduler

%files volume
%defattr(-,root,root,-)
%{_bindir}/nova-volume
%{_initrddir}/%{name}-volume

%if 0%{?with_doc}
%files doc
%defattr(-,root,root,-)
%doc LICENSE doc/build/html
%endif

