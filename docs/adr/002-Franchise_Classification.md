# ADR-002: Franchise Classification Rule

## Status

Accepted

## Problem

The recommendation requires comparison between franchise films and standalone films.

The brief does not define franchise membership.

## Impact

Different classification methods may produce different recommendations and make future reruns inconsistent.

## Decision

A film is classified as a franchise title when TMDb returns a non-null belongs_to_collection value.

A film is classified as standalone when collection information is not available.

## Alternative Considered

### Manual Franchise Identification

Group movies manually using title names and analyst judgement.

### Why Someone Might Choose It

Analysts may identify relationships not represented in TMDb collections.

### Why Rejected

The approach is subjective and difficult for future analysts to reproduce.

## Trade-Off

Repeatability was prioritised over manual flexibility.

## Cost if Wrong

Incomplete collection metadata could cause some franchise films to be classified as standalone titles.

## Evidence

The final recommendation was based on franchise and standalone classifications derived from TMDb collection metadata.