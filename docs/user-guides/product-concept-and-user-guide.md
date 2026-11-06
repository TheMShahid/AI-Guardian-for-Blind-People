# Product Concept and Preliminary User Guide

| Attribute | Value |
|---|---|
| Document ID | USER-001 |
| Version | 1.1 |
| Status | Conceptual guide; not instructions for an available product |
| Related | PID-001, SRS-001, ACC-001, SAF-001, SEC-001, VVP-001 |

## 1. Project intent and availability

AI Guardian for Blind People is being designed as supplementary assistance for selected visual-information tasks. Future versions may support user-initiated text reading, supported object information, or bounded scene descriptions through accessible audio interaction.

This repository currently documents a project in discovery/planning. It is not a finished, implemented, validated, or certified assistive product. This guide describes a possible future interaction concept only.

## 2. Intended interaction concept

A future workflow may be:
1. Open the accessible application or activate a supported connected device.
2. Select or speak a task that is explicitly supported by that release.
3. Review the permission and capture-state information.
4. Initiate capture for the selected request.
5. Receive accessible progress or failure status while processing occurs.
6. Hear a bounded result and any uncertainty or limitation.
7. Stop or replay spoken output, retry where appropriate, or end the session.

Exact controls, supported tasks, languages, devices, and interaction patterns will be designed and evaluated with users. Do not infer that a workflow is available because it appears in this concept document.

## 3. Important limitations and safety

AI can misidentify objects, misread text, omit relevant details, or generate incorrect descriptions. Camera view, lighting, distance, motion, noise, connectivity, and model limitations affect results.

Never rely on this proposed system for safe road crossing, guaranteed obstacle avoidance, emergency decisions, or proof that a path is clear. Continue using established mobility aids and techniques, including a white cane, guide dog, and orientation/mobility training as applicable. The product is not a replacement for human assistance.

## 4. Privacy expectations

A future product should make capture status clear, request permissions at point of use, minimize storage, and explain local/cloud processing. Research or training use requires separate informed authorization. Users should be able to control optional history and understand deletion limitations.

## 5. Failure and uncertainty

If the camera, microphone, network, model service, or connected device is unavailable, the future product should explain the condition accessibly. Poor-quality, stale, incomplete, or uncertain results should not be presented as current and reliable facts. Users should retain control to cancel and stop audio output.

## 6. Publication and release note

Revise this guide before public prototype/release so it reflects tested workflows, supported devices/languages, permissions, data practices, and evidence-based limitations. Remove conceptual language only when actual behavior has been implemented and verified.

## 7. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial product concept and preliminary interaction guide. |
| 1.1 | 2026-11-06 | Strengthened conceptual-only status, safe-use limits, privacy expectations, failure/uncertainty guidance, and publication gate. |
