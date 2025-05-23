<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.desec.dns

Configures DNS entries for deSEC.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for lingfra.desec.dns role

This role implements the deSEC API fields as a YAML structure.
This allows to define the configuration for deSEC in your Ansible inventory alongside your other host configurations.

### Options for `main`

#### `dns_desec_authorization_token`

Type: `str`, **required**.

Authorization token for deSEC API. Can be obtained at [desec.io/tokens](https://desec.io/tokens).

#### `dns_domain_list`

Type: `list of dicts of 'dns_domain_list' options`, Default: `[]`.

List of domains to be managed on your deSEC account. One list item reflects one domain in the account.

**Options:**

- **`name`** (Type: `str`, **required**).

  The domain itself, e. g. `example.com`.

- `rrset_list` (Type: `list of dicts of 'rrset_list' options`, Default: `[]`).

  The Resource Record Sets to add / remove / modify. Refer to the [RRset Field Reference](https://desec.readthedocs.io/en/latest/dns/rrsets.html#rrset-field-reference) in the deSEC DNS API documentation.

  **Options:**

  - `records` (Type: `list of 'str'`, optional).

    Record content strings. Omit this variable or set it to `[]` to delete a record set.

  - **`subname`** (Type: `str`, **required**).

    Subdomain string.

  - `ttl` (Type: `int`, Default: `3600`).

    The time-to-live value for this record set.

  - **`type`** (Type: `str`, **required**).

    The type of the record set.

    **Choices:**

    - `A`
    - `AAAA`
    - `AFSDB`
    - `APL`
    - `CAA`
    - `CDNSKEY`
    - `CDS`
    - `CERT`
    - `CNAME`
    - `DHCID`
    - `DLV`
    - `DNAME`
    - `DNSKEY`
    - `DS`
    - `EUI48`
    - `EUI64`
    - `HINFO`
    - `HTTPS`
    - `KX`
    - `L32`
    - `L64`
    - `LOC`
    - `LP`
    - `MX`
    - `NAPTR`
    - `NID`
    - `NS`
    - `OPENPGPKEY`
    - `PTR`
    - `RP`
    - `SMIMEA`
    - `SPF`
    - `SRV`
    - `SSHFP`
    - `SVCB`
    - `TLSA`
    - `TXT`
    - `URI`

### Examples for `main`

```yaml
---
- name: "Configure deSEC DNS entries over API"
  hosts: localhost
  become: false # no need for root privileges
  gather_facts: false # no need for facts
  tasks:
    - name: "Import role lingfra.desec.dns"
      ansible.builtin.import_role:
        name: lingfra.desec.dns
      vars:
        # it is recommended to encrypt this string with Ansible vault
        dns_desec_authorization_token: 0123456789abcdefghijklmnopqrstuvwxyz

        dns_domain_list:
          - name: example.com
            rrset_list:
              # adds a resource record set for web01
              - subname: web01
                type: A
                ttl: 86400
                records:
                  - 192.168.10.23
                  - 192.168.10.24

              # deletes the AAAA record for db01
              - subname: db01
                type: AAAA
                records: []

              # omitting records also deleted the specified resource record set
              - subname: db01
                type: A
```

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.desec][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://codeberg.org/lingfra/ansible-collection-lingfra-desec
<!-- END_ANSIBLE_DOCS -->
